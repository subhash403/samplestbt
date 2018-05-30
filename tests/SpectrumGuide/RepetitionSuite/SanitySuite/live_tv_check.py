
import os
import sys

# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d

sys.path.insert(0,_get_test_pack_root())

from tests.astro.Sampler import UserWrapper
from tests.SpectrumGuide.Navigate import fromLiveTV
from tests.SpectrumGuide.Navigate import fromAnyScreen
from tests.SpectrumGuide.Navigate import fromCloudGuide


"""
======================================================================================================================
Function Test Coverage : <Sanity_Test_For_Live_TV>
Author      : Beau Yoder 
Description : Test to check if live TV is playing
Reviewed By : TBD
======================================================================================================================
"""


def test_live_tv():
    # Initialize test
    test_name = "sanity_live_tv"
    user = UserWrapper(test_name)
    user.start()
    user.LogResults.info("Test Name :{}".format(test_name))
    assertion_flag = True

    if not fromAnyScreen.exit_to_live_tv_screen("Step 1", user, 3):
        assertion_flag = False

    user.clean_up(assertion_flag)