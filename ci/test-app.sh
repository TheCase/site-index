#!/bin/sh

sh provision.sh
python server.py &
sleep 5
curl http://localhost:5000/ping | grep "pong" && echo "test passed"
