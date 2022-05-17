import os
import hashlib
import datetime
import shutil
import json
import socket

import Log

log = Log.get_logger(__name__)

def set_tmp_path(process_type,hash_id):
    try:
        temp_path = f"../temp/{process_type}/{hash_id}"
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        return temp_path
    except Exception as e:
        log.error(f'ERROR -> {e}')
        raise

def remove_dir(tmp_path):
    try:
        shutil.rmtree(tmp_path)
    except Exception as e:
        log.error(f'ERROR -> {e}')
        raise

def hash_text(b64_str):
    try:
        date_now = datetime.datetime.strftime(datetime.datetime.today(), '%Y%m%d%H%M%S')
        hash_code = hashlib.md5(bytes(b64_str, 'utf-8')).hexdigest()
        return f"{date_now}{hash_code}"
    except Exception as e:
        log.error(f'ERROR -> {e}')
        raise

def get_properties(process_type):
    try:
        json_data = json.load(open(f'properties/{process_type.lower()}.json',encoding='utf-8'))
        return json_data
    except Exception as e:
        log.error(f'ERROR -> {e}')
        raise

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        log.error(f'ERROR -> {e}')
        raise
