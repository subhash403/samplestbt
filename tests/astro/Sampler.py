import logging
import os
import time
import traceback

import stbt

from tests import configuration

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class UserWrapper:
    def __init__(self,test_name):
        self.test_name = test_name
        self.version = "stbt-1.0.0"

    @staticmethod
    def start():
        pass

    @staticmethod
    def get_current_date_time_stamp():
        return time.strftime("%Y:%m:%d-%I:%M:%S%p")

    @staticmethod
    def file_exists(file_path):
        return os.path.isfile(file_path)

    def write_to_file(self, file_path, text):
        try:
            if self.file_exists(file_path):
                file_obj = open(file_path, 'a')
            else:
                file_obj = open(file_path, 'w')
            if file_obj:
                file_obj.write(text)
                file_obj.close()
                return True
            else:
                return False
        except:
            self.LogResults.error("File Write Error '{}' - Found, Error - ".format(traceback.format_exc()))
            return False

    def remote_control_press_until_image_match(self, key, image_to_find, region=None, maximum_key_press=5):
        if region is not None:
            img_region = stbt.Region(region["x"], region["y"], width=region["width"], height=region["height"])
            return stbt.press_until_match(key, image_to_find, max_presses=maximum_key_press, region=img_region)
        else:
            return stbt.press_until_match(key, image_to_find, max_presses=maximum_key_press)

    def remote_control_press(self,key, number_of_times=1):
        self.LogResults.info("Remote Control Key <{}> pressed {} time(s)".format(key, number_of_times))
        for i in range(0,number_of_times+1) :
            stbt.press(str(key))

    def check_image(self, image_to_find, region=None, timeout_secs=configuration.image_check_time_out_secs):
        image_name = image_to_find.split("/")[-1:][0]
        if region is not None:
            img_region = stbt.Region(region["x"], region["y"], width=region["width"], height=region["height"])
            if stbt.wait_until(lambda: stbt.match(image_to_find, region=img_region), timeout_secs=timeout_secs):
                self.LogResults.info("Image check passed using: {}".format(image_name))
                return True
            else:
                self.LogResults.warning("Image check failed using: {}".format(image_name))
                return False
        else:
            if stbt.wait_until(lambda: stbt.match(image_to_find), timeout_secs=timeout_secs):
                self.LogResults.info("Image check passed using: {}".format(image_name))
                return True
            else:
                self.LogResults.warning("Image check failed using: {}".format(image_name))
                return False

    def check_motion(self, motion_timeout):
        if stbt.wait_for_motion(motion_timeout):
            self.LogResults.info("Motion detected")
            return True
        else:
            self.LogResults.warning("Motion is not detected")
            return False

    def check_text(self, text_to_check, region, timeout_secs = configuration.image_check_time_out_secs):
        try:
            start_time = time.time()
            is_txt_found = False
            while True:
                if time.time() -  start_time > timeout_secs :
                    break
                txt_region = stbt.Region(region["x"], region["y"], width=region["width"], height=region["height"])
                ocr_txt = stbt.ocr(region=txt_region)
                ocr_txt.strip()
                if text_to_check in ocr_txt:
                    is_txt_found = True
                    self.LogResults.info("Text {} - Found".format(text_to_check))
                    break
                time.sleep(1)
            return is_txt_found
        except:
            self.LogResults.error("Text {} - Found".format(traceback.format_exc()))

    def get_text(self, region):
        try:
            txt_region = stbt.Region(region["x"], region["y"], width=region["width"], height=region["height"])
            ocr_txt = stbt.ocr(region=txt_region)
            ocr_txt = ocr_txt.strip()
            self.LogResults.info("Captured Text : {}".format(ocr_txt))
        except:
            self.LogResults.error("Text {} - Found".format(traceback.format_exc()))
            ocr_txt = None

        return ocr_txt

    class LogResults:

        @staticmethod
        def passed(message):
            print("PASS: {}".format(message))

        @staticmethod
        def failed(message):
            try :
                assert False, "Reason - {}".format(message)
            except:
                print ("FAIL: {}".format(message))

        @staticmethod
        def error(message):
            print("ERROR: {}".format(message))

        @staticmethod
        def info(message):
            print("INFO: {}".format(message))

        @staticmethod
        def warning(message):
            print("WARN: {}".format(message))

    def clean_up(self, assertion_flag):
        assert assertion_flag, "Test case : {} failed".format(self.test_name)
        return True
