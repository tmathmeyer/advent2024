
from functools import cmp_to_key

def roib(rlz, l):
  cmp = lambda x,y: -1 if (x,y) in rlz else 1
  x = list(sorted(l, key=cmp_to_key(cmp)))
  return x if x != l else None

def p1():
  with open('input.txt', 'r') as f:
    res = 0
    rlz = set()
    for line in f.readlines():
      if '|' in line:
        rlz.add(tuple(line.strip().split('|')))
      elif ',' in line:
        test = list(line.strip().split(','))
        if roib(rlz, test) is None:
          res += int(test[len(test)//2])
    print(res)

def p2():
  with open('input.txt', 'r') as f:
    res = 0
    rlz = set()
    for line in f.readlines():
      if '|' in line:
        rlz.add(tuple(line.strip().split('|')))
      elif ',' in line:
        if n := roib(rlz, list(line.strip().split(','))):
          res += int(n[len(n)//2])
    print(res)





import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
locals()[sys.argv[1]]()