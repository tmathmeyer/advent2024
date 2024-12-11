
import math
import functools

@functools.cache
def n2s(n, i):
  if i == 0:
    return 1
  if n == 0:
    return n2s(1, i-1)
  d = int(math.log10(n))+1
  if d%2 == 0:
    d = int(10**(d/2))
    return n2s(n%d, i-1) + n2s(n//d, i-1)
  return n2s(n*2024, i-1)

def p1(file):
  print(sum(n2s(int(x), 25) for x in file.read().strip().split(' ')))

def p2(file):
  print(sum(n2s(int(x), 75) for x in file.read().strip().split(' ')))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)