"""FileName : oslib.py

   Brief: This is a reusable library file for performing the most common file handling,time string and os related tasks

   Author:  SivaRam Kumar Mani
"""
import base64
import datetime
import logging
import os
import platform
import subprocess
import threading
import time
import traceback
from datetime import datetime


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def get_os_name():
    return platform.system().upper()


def get_os_info():
    logger.debug()
    return platform.system(), platform.release(), os.name


def join_paths(main_path, *arg):
    for pth in arg:
        main_path = os.path.join(str(main_path), str(pth))
    main_path = os.path.abspath(main_path)
    return main_path


def format_path(path):
    return os.path.abspath(path)


def get_root_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        logging.warning("Path : {0} already exist, Cannot recreate".format(path))


def create_directory(directory_path):
    if not (os.path.isdir(directory_path)):
        os.mkdir(directory_path)
        return 1
    else:
        logging.warning("Folder :  {0} already exist, Cannot recreate")
        return 0



def get_current_date_time_stamp():
    return time.strftime("%Y%m%d_%I%M%S%p")


def get_current_time_stamp():
    return time.strftime("%I%M%S%p")


def get_sql_time_stamp():
    sql_date_time = datetime.datetime.now().strftime("%H_%M_%S")
    return sql_date_time.replace("_", ":")


def get_sql_date():
    return time.strftime("%Y-%m-%d")


def get_current_date():
    return time.strftime("%Y%m%d")


def directory_exists(dir_path):
    return os.path.isdir(dir_path)


def file_exists(file_path):
    return os.path.isfile(file_path)


def create_file(file_path):
    try:
        open(file_path, 'a').close()
        return 1
    except:
        logging.error("Create File Error : {}".format(traceback.format_exc()))
        return 0


def delete_directory(dir_path):
    try:
        os.rmdir(dir_path)
        return 1
    except:
        return 0


def delete_file(file_path):
    try:
        os.remove(file_path)
        return 1
    except :
        return 0


def move_file(file_path, new_path):
    try:
        os.rename(file_path, new_path)
        return 1
    except :
        return 0


def move_directory(current_dir_path, new_dir_path):
    try:
        os.rename(current_dir_path, new_dir_path)
        return 1
    except:
        return 0


def write_to_file(file_path, text):
    try:
        if file_exists(file_path) :
            file_obj = open(file_path, 'a')
        else :
            file_obj = open(file_path, 'w')
        if file_obj:
            file_obj.write(text)
            file_obj.close()
            return True
        else:
            return False
    except:
        return False


def get_csv_row_count(file_path, ignore_header=False):
    row_count = sum(1 for line in open(file_path))
    if ignore_header:
        row_count = row_count -1
    return row_count


def command_line_execute(cmd):
    start_time = datetime.datetime.now()
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    proc_id = proc.pid
    proc.wait()
    stdout, stderr = proc.communicate()
    return_code = proc.returncode
    logging.info("Process ID : {} , Exit Status : {}\nOutput : {}\nError : {}".format(proc_id, return_code, stdout, stderr))
    logging.info("Process execution time :  -  {} Seconds".format(datetime.datetime.now() - start_time))
    return return_code, stdout,stderr


class ExecuteCommand(threading.Thread) :
    def __init__(self, command_list):
        super(ExecuteCommand, self).__init__()
        self.stdout = None
        self.stderr = None
        self.stopCap = False
        self.stopExec = False
        self.returnCode = -1
        self.command_list = command_list
        self.proc = None
        self.proc_id = 0

    def run(self):
        try :
            self.proc = subprocess.Popen(self.command_list,
                                         shell=False,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
            self.proc_id = self.proc.pid
            self.proc.wait()
            self.stdout, self.stderr = self.proc.communicate()
            self.returnCode = self.proc.returncode
        except :
            logging.error("Error while Executing : {}".format(self.command_list))
            print(traceback.format_exc())

    def get_status(self):
        return self.returnCode

    def get_output(self):
        return self.stdout


def encode(txt):
    key = "zaq1@WSXcde3$RFVbgt5^YHNmju7*IK<.lo9)P:?'[-+}"
    enc = []
    for i in range(len(txt)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(txt[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))


def decode(enc):
    enc = str(enc)
    key = "zaq1@WSXcde3$RFVbgt5^YHNmju7*IK<.lo9)P:?'[-+}"
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        print(dec_c)
        dec.append(dec_c)
    return "".join(dec)


def get_parent_path(path):
    return os.path.dirname(path)


def set_logger(logger_name, logger_level):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logger_level)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        return logger


def get_unix_epoch_time():
    dt = datetime.now()
    return dt.microsecond


def get_time_stamp_from_epoch(epoch_time):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))


def get_user_home_path():
    from os.path import expanduser
    return expanduser("~")


def delete_all_files(directory_path):
    file_list = [f for f in os.listdir(directory_path)]
    for f in file_list:
        logging.info("Deleting file : {} ...".format(f))
        os.remove(os.path.join(directory_path, f))


def delete_all_files_contains(directory_path, file_name_contains):
    file_list = [f for f in os.listdir(directory_path) if file_name_contains in f]
    for f in file_list:
        logging.info("Deleting file : {} ...".format(f))
        os.remove(os.path.join(directory_path, f))


def delete_all_files_bytype(directory_path, file_type):
    file_list = [f for f in os.listdir(directory_path) if f.endswith(".{}".format(file_type))]
    for f in file_list:
        logging.info("Deleting file : {} ...".format(f))
        os.remove(os.path.join(directory_path, f))
