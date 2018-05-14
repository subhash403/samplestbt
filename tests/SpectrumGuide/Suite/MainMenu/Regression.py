import logging
import os
import sys


# # Workaround for import path behaviour; can be removed once stb-tester v29 is released.
# def _get_test_pack_root():
#     d = os.path.dirname(os.path.abspath(__file__))
#     #print "dirName : %s" %d
#     while not os.path.exists(os.path.join(d, ".stbt.conf")):
#         d = os.path.dirname(d)
#         print "dirName : %s" %d
#     print "===> Final Root Path ==>  {}".format(d)
#     return d

# Workaround for import path behaviour; can be removed once stb-tester v29 is released.
def _get_test_pack_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, ".stbt.conf")):
        d = os.path.dirname(d)
        sys.path.insert(0, d)
        print "Info : Inserting Path : {} to path".format(d)
    return d


from tests.SpectrumGuide.Navigate import Live_TV
result_file = "{}/status_by_step.csv".format(os.path.dirname(os.path.abspath(__file__)))

def test_tc01_demo_framework():
    """ This is a simple test to illustrate the how the framework structure works """
    test_case_name = "test_tc01_demo_framework"
    Live_TV.go_to_main_menu()
