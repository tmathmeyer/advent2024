import numpy as np

def pf(f, off=0):
  a = (0, 0)
  b = (0, 0)
  for l in f.readlines():
    t = l.strip().split(' ')
    if not t[0]:
      continue
    if t[1] == 'A:':
      a = (int(t[2][2:-1]), int(t[3][2:]))
    elif t[1] == 'B:':
      b = (int(t[2][2:-1]), int(t[3][2:]))
    elif t[0]:
      yield (a, b, (int(t[1][2:-1])+off, int(t[2][2:])+off))


def fsq(a, b, p):
  solv = np.linalg.solve(np.array([[a[0], b[0]],[a[1], b[1]]]),np.array(p))
  chx = np.round(solv[0])*a[0] + np.round(solv[1])*b[0]
  chy = np.round(solv[0])*a[1] + np.round(solv[1])*b[1]
  if (int(chx), int(chy)) == p:
    return (np.round(solv[0]), np.round(solv[1]))
  return None, None


def p1(file):
  sum = 0
  for a, b, p in pf(file):
    x, y = fsq(a, b, p)
    if x is not None:
      sum += (3*x + y)
  print(sum)


def p2(file):
  sum = 0
  for a, b, p in pf(file, 10000000000000):
    x, y = fsq(a, b, p)
    if x is not None:
      sum += (3*x + y)
  print(sum)


import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)