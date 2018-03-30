#!/bin/sh
for i in $(seq 1 2); do
 echo "*********************** Try: $i *******************************"
 sshpass -p "Charter1" ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@172.30.82.139 "python dvr_status.py 30.255.240.82"
 python stbt_rig.py -v --node-id=stb-tester-00044b80f5f9 run tests/reboot_test.py::test_DVR_on_reboot
 expect "Enter Access Token for portal https://charter.stb-tester.com:"
 send "b8V_zD5Aaz1cGqPwYQAuDK9p9-6Am2JP"
 expect "Please enter password for encrypted keyring:"
 send "Skittles1997!"
 expect "Username for 'https://github.com':"
 send "prayfran2018"
 expect "Password for 'https://prayfran2018@github.com':"
 send "Skittles1997!" 
done
