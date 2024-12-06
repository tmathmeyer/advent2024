
import re
def p1():
  with open('input.txt', 'r') as f:
    print(sum(int(x)*int(y) for x,y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', f.read())))

def p2():
  with open('input.txt', 'r') as f:
    sum = 0
    for _,a,b,y,n in re.findall(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))", f.read()):
      if y != '': sum = abs(sum)
      if n != '': sum = 0 - abs(sum)
      if a and b and sum>=0: sum += int(a)*int(b)
    print(abs(sum))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
locals()[sys.argv[1]]()