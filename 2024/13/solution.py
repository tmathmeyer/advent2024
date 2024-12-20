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


def fsqnnp(a, b, p):
  n = p[0]*b[1] - p[1]*b[0]
  d = a[0]*b[1] - a[1]*b[0]
  if n == 0:
    raise Exception(f'{a} and {b} are parallel')
  if n % d == 0:
    A = int(n / d)
    return A, int((p[0] - a[0]*A) // b[0])
  return None, None


def p1(file):
  sum = 0
  for a, b, p in pf(file):
    x, y = fsqnnp(a, b, p)
    if x is not None:
      sum += (3*x + y)
  print(sum)


def p2(file):
  sum = 0
  for a, b, p in pf(file, 10000000000000):
    x1, y1 = fsqnnp(a, b, p)
    if x1 is not None:
      sum += (3*x1 + y1)
  print(sum)


import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)