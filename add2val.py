#!/usr/bin/python

import sys
import calc

argnum = len(sys.argv) - 1

print(len(sys.argv))
print(argnum)

if argnum == 2:
  print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
  sys.exit(0)
else:
  print("The correct syntax is add2vale argv1 argv2")
  sys.exit(1)
 

