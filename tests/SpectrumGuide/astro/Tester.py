import stbt

def press_until_image_match(image_to_find, maximum_key_press=5):
    return stbt.press_until_match(image_to_find, max_presses=maximum_key_press)

def press(key, times=1):
    for _ in " " * times: stbt.press(str(key))

def check_image(image_to_find,timeout_secs=10):
    return stbt.wait_until(lambda: stbt.match(image_to_find), timeout_secs=timeout_secs)

def check_motion(timeout):
    return stbt.wait_for_motion(timeout)

def get_text(region=None):
    try:
        txt_region = stbt.Region(region["x"], region["y"], region["width"], region["height"])
        ocr_text = stbt.ocr(txt_region)
        ocr_text.strip()
        return ocr_text
    except ValueError:
        return None

def check_text(text_to_check,region=None):
    if region is not None:
        txt_region = stbt.Region(region["x"], region["y"], region["width"], region["height"])
        ocr_txt = stbt.ocr(txt_region)
        ocr_txt.strip()
        if text_to_check in ocr_txt:
            return True
        else:
            return False

def launch_guide():
    press('KEY_GUIDE')
    assert check_image(guide_options.png), \
    "Guide not launched from Live TV within 10 seconds"