# -*- coding: utf8 -*-
__organization__ = 'Zodiac Interactive'

import os
import sys
import time
import datetime

class STB_reboot(object):

    def __init__(self, input):
        self.execute_boxes(input)

    def execute_boxes(self,input):
            self.reboot(input)


    def send_command_internal(self, command, box_ip, timeout=10.0):
        import socket
        result = ""
        port = 65432
        #print('Sending command "%s" to %s:%d' % (command, box_ip, port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        try:
            sock.connect((box_ip, port))
            sock.send(command)
            #print('"%s" command' % (command))
        except Exception as ex:
            print('"%s" command execution failed!' % command)
            print(ex)
        finally:
            sock.close()

    def reboot(self, box_ip):

        command0 ="osdiag rebootnow"

        data = self.send_command_internal(command0, box_ip)

if __name__ == '__main__':
    t0 = time.time()
    if len(sys.argv) != 2:
        print('Usage: \npython MotoReboot.py file_with_ip.txt')
        os._exit(1)
    stat = STB_reboot(sys.argv[1])
    print(time.time() - t0)
