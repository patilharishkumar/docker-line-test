#!/bin/bash
uuid=$(curl  -d "to=100" -X POST http://127.0.0.1/counter/)
echo $uuid
curl -X GET http://127.0.0.1/counter/$uuid
sleep 1 && curl -X GET http://127.0.0.1/counter/$uuid
