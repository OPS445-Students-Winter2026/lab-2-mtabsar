#!/usr/bin/env python3
import sys
#Author: Mohd Tahsin Absar
#Author ID - 102192234
#Date Created - 2026/05/03

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
elif len(sys.argv) == 1:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer-1

print('blast off!')