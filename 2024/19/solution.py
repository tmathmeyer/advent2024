
import functools

def rf(f):
  it = iter(f.readlines())
  towels = tuple(set(next(it).strip().split(', ')))
  next(it)
  return towels, [l.strip() for l in it]

@functools.cache
def cp(t, p, ml):
  if not p:
    return 1
  result = 0
  for L in range(min(ml, len(p))):
    L = L+1
    A, B = p[:L], p[L:]
    if A in t:
      if cnt := cp(t, B, ml):
        result += cnt
  return result

def p1(file):
  t, ps = rf(file)
  ml = max(len(tt) for tt in t)
  mps = []
  for p in ps:
    if cp(t, p, ml):
      mps.append(p)
  print(len(mps))

def p2(file):
  t, ps = rf(file)
  ml = max(len(tt) for tt in t)
  sum = 0
  for p in ps:
    sum += cp(t, p, ml)
  print(sum)

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)