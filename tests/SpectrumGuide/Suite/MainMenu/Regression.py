import os
import subprocess
import sys


# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    #print "dirName : %s" %d
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
        print "dirName : %s" %d
    print "===> Final Root Path ==>  {}".format(d)
    return d

_root_path = _get_test_pack_root()

sys.path.insert(0, _root_path)

# print "INSERTING  : {}".format("{}/NavigateTo".format(_root_path))
# sys.path.insert(0,"{}/NavigateTo".format(_root_path))
#
# print "INSERTING  : {}".format("{}/ObjectRepo".format(_root_path))
# sys.path.insert(0,"{}/ObjectRepo".format(_root_path))
#
# print "INSERTING  : {}".format("{}/SetupTearDown".format(_root_path))
# sys.path.insert(0,"{}/SetupTearDown".format(_root_path))

from tests.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
from tests.SpectrumGuide.NavigateTo import LiveTV


def test_tc01_demo_framework():
    """ This is a simple test to illustrate the how the framework structure works """
    Tester.LogResults.info("Executing Test - test_tc01_demo_framework")
    LiveTV.to_main_menu()
