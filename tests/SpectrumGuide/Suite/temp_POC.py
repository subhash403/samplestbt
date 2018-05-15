import os
import sys

# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    print "dirName : %s" % d
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
        print "dirName : %s" % d
    return d

sys.path.insert(0, _get_test_pack_root())


from tests.astro import Tester

def test_logging():
    Tester.LogResults.passed("Step 1 did a thing")
    Tester.remote_control_press('KEY_MENU')