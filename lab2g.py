#!/usr/bin/env python3

#Author: Marc Joven Velota
#Author ID: mjvelota
#Date Created: 2020/09/29

import sys


if len(sys.argv) == 2:
	timer = int(sys.argv[1])
	while timer != 0:
		
		print(timer)

		timer = timer - 1
else:
	timer = 3 
	while timer != 0:
		print(timer)
		timer = timer -1

print('blast off!')
