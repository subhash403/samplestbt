import stbt

def press_key(key, times):
    for _ in " " * times:stbt.press(str(key))

