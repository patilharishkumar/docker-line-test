#!/bin/bash
# Tested using bash version 4.1.5
for ((i=1;i<=100;i++)) do curl -s http://127.0.0.1; done | sort --unique
