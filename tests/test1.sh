#!/bin/bash
ip="30.255.240.82"
group=$2
echo "osdiag rebootnow" | ./mototerm "$ip" &
pid=$!
sleep 5
kill ${pid}

