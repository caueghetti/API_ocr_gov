from datetime import datetime
import logging
from sys import argv
import pymsteams

def get_logger(logger_name):
    path_file_log=f'../log/log_ocr_{datetime.now().strftime("%Y%m%d")}.log'
    logging.basicConfig(
        filename=path_file_log,
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'"
    )
    logger = logging.getLogger(logger_name)

    Stream_Handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    Stream_Handler.setFormatter(formatter)
    
    logger.addHandler(Stream_Handler)

    return logger