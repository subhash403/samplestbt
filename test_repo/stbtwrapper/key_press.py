import stbt

def press(key, times=1):
    for _ in " " * times:stbt.press(str(key))

