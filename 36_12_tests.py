import stbt

channels = [1,2,3,4,5,6,7,8,9]
for ch in channels:
    for x in list(ch): stbt.press('KEY_'+'x')
    assert stbt.wait_for_motion()
