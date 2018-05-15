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

from tests.SpectrumGuide.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScree