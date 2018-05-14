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

# # Workaround for import path behaviour; can be removed once stb-tester v29 is released.
# def _get_test_pack_root():
#     d = os.path.dirname(os.path.abspath(__file__))
#     print ("Absolute Path : {}".format(d))
#     while not os.path.exists(os.path.join(d, ".stbt.conf")):
#         d = os.path.dirname(d)
#         sys.path.insert(0, d)
#         # Add the module directory to sys.path
#         #sys.path.append(d)
#         print "Info : Appending Module Path : {} to path".format(d)
#     return d
# sys.path.insert(0, _get_test_pack_root())

#print "ABSOLUTE PATH : {}".format(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def runProcess(exe):
    ## call date command ##
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    ## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
    ## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
    ## or None, if no data should be sent to the child.
    (output, err) = p.communicate()

    ## Wait for date to terminate. Get return returncode ##
    p_status = p.wait()
    print "Command output : ", output
    print "Command exit status/return code : ", p_status

_root_path = _get_test_pack_root()

sys.path.insert(0,_root_path)

print "INSERTING  : {}".format("{}/NavigateTo".format(_root_path))
sys.path.insert(0,"{}/NavigateTo".format(_root_path))

print "INSERTING  : {}".format("{}/ObjectRepo".format(_root_path))
sys.path.insert(0,"{}/ObjectRepo".format(_root_path))

print "INSERTING  : {}".format("{}/SetupTearDown".format(_root_path))
sys.path.insert(0,"{}/SetupTearDown".format(_root_path))


from tests.astro import Tester
from tests.SpectrumGuide.ObjectRepo import MainMenuScreen
#from tests.SpectrumGuide.NavigateTo import LiveTV


def test_tc01_demo_framework():
    print "Main Menu Image : {}".format(MainMenuScreen.Spectrum_Logo["image"])
    #runProcess(["pwd"])
    runProcess('pwd')
    runProcess('ls {}/tests'.format(_root_path))
    """ This is a simple test to illustrate the how the framework structure works """
    test_case_name = "test_tc01_demo_framework"
    #LiveTV.to_main_menu()
