import logging
import os
import time
import stbt

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def get_current_date_time_stamp():
    return time.strftime("%Y:%m:%d-%I:%M:%S%p")

def file_exists(file_path):
    return os.path.isfile(file_path)

def write_to_file(file_path, text):
    try:
        if file_exists(file_path) :
            file_obj = open(file_path, 'a')
        else :
            file_obj = open(file_path, 'w')
        if file_obj:
            file_obj.write(text)
            file_obj.close()
            return True
        else:
            return False
    except:
        return False


def remote_control_press_untill_image_match(image_to_find, maximum_key_press=5):
    return stbt.press_until_match(image_to_find, max_presses=maximum_key_press)


def remote_control_press(key, times=1):
    LogResults.info("Remote Control Key <{}> pressed {} time(s)".format(key, times))
    for _ in " " * times: stbt.press(str(key))


def check_image(image_to_find,timeout_secs=10):
    if stbt.wait_until(lambda: stbt.match(image_to_find), timeout_secs=timeout_secs):
        return True
    else:
        LogResults.warning("Image check failed using: {}".format(image_to_find))
        return False


def check_motion(timeout):
    return stbt.wait_for_motion(timeout)

def check_text(text_to_check,region=None):
    if not region is None:
        txt_region = stbt.Region(region["x"], region["y"], region["width"], region["height"])
        ocr_txt = stbt.ocr(txt_region)
        ocr_txt.strip()
        if text_to_check in ocr_txt:
            return True
        else:
            return False


class LogResults:

    @staticmethod
    def passed(message):
        print("PASS: {}".format(message))

    @staticmethod
    def failed(message):
        assert False, "Reason - {}".format(message)

    @staticmethod
    def error(message):
        print("ERRO: {}".format(message))

    @staticmethod
    def info(message):
        print("INFO: {}".format(message))

    @staticmethod
    def warning(message):
        print("WARN: {}".format(message))

