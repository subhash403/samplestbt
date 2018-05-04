import stbt

def press_key(key, times=1):
    for _ in " " * times:stbt.press(str(key))

