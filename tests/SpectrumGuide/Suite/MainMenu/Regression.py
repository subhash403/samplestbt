import os
import subprocess
import sys

# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
    return d

_root_path = _get_test_pack_root()

sys.path.insert(0, _root_path)

from tests.astro import Tester
from tests.SpectrumGuide.NavigateTo import LiveTV


def test_tc01_demo_framework():
    """ This is a simple test to illustrate the how the framework structure works """
    Tester.LogResults.info("Executing Test - test_tc01_demo_framework")
    LiveTV.to_main_menu()
