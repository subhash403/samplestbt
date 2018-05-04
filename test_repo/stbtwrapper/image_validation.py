import stbt

#Method for waiting until an action occurs
#Optional variables: timeout which determines how long to wait defaults to 10 seconds
#Example of Wait until something disappears: pass (lambda: not match("xyz.png")) as action
#Eaxmple of Assert that two images are present at the same time: pass (lambda: match("a.png") and match("b.png")) as action
def wait_until(action,fail_message,timeout=10):
    assert stbt.wait_until(action,timeout), \
    str(fail_message)

#Method for waiting until motion is detected
#Optional variables: timeout which determines how long to wait defaults to 10 seconds
def wait_for_motion(fail_message, timeout=10):
    assert stbt.wait_for_motion(timeout), \
    str(fail_message)

#Method for waiting until an image appears
#Optional variables: timeout which determines how long to wait defaults to 10 seconds
def wait_for_match(image,fail_message,timeout=10):
    assert stbt.wait_for_match(str(image),timeout), \
    str(fail_message)

