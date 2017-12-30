#!/bin./sh

cd develop
sh provision.sh
python server.py &
sleep 5
curl http://localhost:5000/health | grep "OK" && echo "test passed"
