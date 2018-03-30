#!/bin/sh
for i in $(seq 1 100); do
 echo "*********************** Try: $i *******************************"
 sshpass -p "Charter1" ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@172.30.82.139 "python dvr_status.py 30.255.240.82"
 #python stbt_rig.py -v --node-id=stb-tester-00044b80f5f9 run tests/example_tests.py::test_DVR_on_reboot
 python stbt_rig.py -v --node-id=stb-tester-00044b80f5f9 run tests/reboot_test.py::test_DVR_on_reboot
done
