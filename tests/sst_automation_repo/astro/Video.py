import stbt

class Tester:
    def __init__(self):
        pass

    def press_untill_image_match(self,image_to_find, maximum_key_press=5):
        return stbt.press_until_match(image_to_find, max_presses=maximum_key_press)

    def press(self,key, times=1):
        for _ in " " * times: stbt.press(str(key))

    def check_image(image_to_find,timeout_secs=10):
        return stbt.wait_until(lambda: stbt.match(image_to_find), timeout_secs=timeout_secs)

    def check_motion(self):
        return stbt.wait_for_motion(timeout)

    def check_text(self,text_to_check,region=None):
        if not region is None:
            txt_region = stbt.Region(region["x"], region["y"], region["width"], region["height"])
            ocr_txt = stbt.ocr(txt_region)
            ocr_txt.strip()
            if text_to_check in ocr_txt:
                return True
            else:
                return False
