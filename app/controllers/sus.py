from flask import Flask,request
from flask_restx  import Api, Resource

from server.instance import server
import Log
import ConvertImage
import Configs
import ExtractImageData

log = Log.get_logger(__name__)
app,api = server.app, server.api
api = api.namespace('SUS',description='Operations related to SUS OCR')

@api.route("/vacinas",methods=['POST'])
class GetCNHInfoFromPDF(Resource):
    def post(self,):
        try:
            log.info('Reciving Requests')
            base64_str = request.get_json(silent=True)
            if base64_str is None:
                return {"error":"Bad Request - base64_str key not found"}
            elif "base64_file" not in base64_str.keys():
                return {"error":"Bad Request - base64_str key not found"}

            base64_str = base64_str['base64_file'].strip()
            hash_id = Configs.hash_text(base64_str)
            temp_path = Configs.set_tmp_path("cnh",hash_id)
            
            log.info(f'Starting process of base64 - {base64_str[:30]}... - PDF - {hash_id}')
            rs = ConvertImage.convert_base64_to_pdf(base64_str,temp_path,hash_id)
            if rs is not None:
                return {"error_1":rs}
            ConvertImage.convert_pdf_from_path(temp_path,hash_id)
            
            fields = Configs.get_properties("cnh")['fields']
            image = ExtractImageData.open_image(temp_path,hash_id)
            r_payload = {}
            for field in fields.keys():
                log.info(f'Processing {field} for {hash_id}')
                crop_image = ExtractImageData.crop_image(image,fields[field]['points'],hash_id)
                crop_image = ExtractImageData.set_threshold_binarize_array(crop_image,fields[field]['threshold'],hash_id)
                if "parms" in fields[field]:
                    parms = fields[field]['parms']
                else: 
                    parms = ''
                r_payload[field] = ExtractImageData.image_to_text(crop_image,fields[field]['psm'],parms,hash_id).strip()
            Configs.remove_dir(temp_path)
            return r_payload
        except Exception as e:
            log.error(e)
            Log.send_alert_error(e)
            return {"error":e}

@api.route("/crlv")
class GetCRLVInfoFromPDF(Resource):
    def post(self,):
        try:
            log.info('Reciving Requests')
            base64_str = request.get_json(silent=True)
            if base64_str is None:
                return {"error":"Bad Request - base64_str key not found"}
            elif "base64_file" not in base64_str.keys():
                return {"error":"Bad Request - base64_str key not found"}
                
            base64_str = base64_str['base64_file'].strip()
            hash_id = Configs.hash_text(base64_str)
            temp_path = Configs.set_tmp_path("crlv",hash_id)
            
            log.info(f'Starting process of base64 - {base64_str[:30]}... - PDF - {hash_id}')
            rs = ConvertImage.convert_base64_to_pdf(base64_str,temp_path,hash_id)
            if rs is not None:
                return {"error_1":rs}
            ConvertImage.convert_pdf_from_path(temp_path,hash_id)
            
            fields = Configs.get_properties("crlv")['fields']
            image = ExtractImageData.open_image(temp_path,hash_id)
            r_payload = {}
            for field in fields.keys():
                log.info(f'Processing {field} for {hash_id}')
                crop_image = ExtractImageData.crop_image(image,fields[field]['points'],hash_id)
                crop_image = ExtractImageData.set_threshold_binarize_array(crop_image,fields[field]['threshold'],hash_id)
                if "parms" in fields[field]:
                    parms = fields[field]['parms']
                else: 
                    parms = ''
                r_payload[field] = ExtractImageData.image_to_text(crop_image,fields[field]['psm'],parms,hash_id).strip()
            Configs.remove_dir(temp_path)
            return r_payload
        except Exception as e:
            log.error(e)
            Log.send_alert_error(e)
            return {"error":e}