from pdf2image import convert_from_path, convert_from_bytes
import base64

import Log

log = Log.get_logger(__name__)

def convert_pdf_from_path(tmp_path,process_id):
    try:
        log.info(f'Cnverting PDF to Image - {process_id}')
        images = convert_from_path(f"{tmp_path}/{process_id}.pdf",poppler_path=r'..\libs\poppler-0.68.0\bin')
        
        for image in images:
            image.save(f'{tmp_path}/{process_id}.jpg','JPEG')
            break
    except Exception as e:
        log.error(e)
        raise

def convert_base64_to_pdf(b64_str,tmp_path,process_id):
    try:
        log.info(f'Converting bs64 to PDF - {process_id}')
        b64_bytes = base64.b64decode(b64_str, validate=True)
        if b64_bytes[0:4] != b'%PDF':
            raise ValueError('Missing the PDF file signature')

        file_path = f"{tmp_path}/{process_id}.pdf"
        with open(file_path, 'wb') as arq:
            arq.write(b64_bytes)
            arq.close()
        return None
    except ValueError as ve:
        log.error(ve)
        return ve
    except Exception as e:
        log.error(e)
        raise

def convert_base64_to_img(b64_str,tmp_path,process_id):
    try:
        log.info(f'Converting bs64 to IMG - {process_id}')
        b64_bytes = base64.b64decode(b64_str, validate=True)

        file_path = f"{tmp_path}/{process_id}.jpg"
        with open(file_path, 'wb') as arq:
            arq.write(b64_bytes)
            arq.close()
    except Exception as e:
        log.error(e)
        raise