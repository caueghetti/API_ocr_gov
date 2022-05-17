import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'..\libs\Tesseract-OCR\tesseract.exe'
from PIL import Image
import numpy as np

import Log

log = Log.get_logger(__name__)

def set_threshold_binarize_array(image, threshold,hash_id):
    try:
        if threshold == 0:
            return image

        log.info(f'Setting threshold {hash_id}')
        """Binarize a numpy array."""
        numpy_array = np.array(image)
        for i in range(len(numpy_array)):
            for j in range(len(numpy_array[0])):
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                else:
                    numpy_array[i][j] = 0
        new_image  = Image.fromarray(numpy_array)
        return new_image
    except Exception as e:
        log.error(f"{hash_id}-{e}")
        raise



def open_image(temp_path,file_name):
    try:
        log.info(f'Opening image - {file_name}.jpg')
        return Image.open(f"{temp_path}/{file_name}.jpg").convert('L')
    except Exception as e:
        log.error(f"{file_name}-{e}")
        raise

def crop_image(image,layout_crop,hash_id):
    try:
        log.info(f'Cropping image {hash_id}')
        image = image.crop(layout_crop)
        return image
    except Exception as e:
        log.error(f"{hash_id}-{e}")
        raise

def image_to_text(image,psm,parms,hash_id):
    try:
        content = pytesseract.image_to_string(image, config = f'--psm {psm} {parms}')
        return content
    except Exception as e:
        log.error(f"{hash_id}-{e}")
        raise

def resize_image(image,size,hash_id):
    try:
        log.info(f'Resizing image {hash_id}')
        image = image.resize(size, Image.ANTIALIAS)
        return image
    except Exception as e:
        log.error(f"{hash_id}-{e}")
        raise