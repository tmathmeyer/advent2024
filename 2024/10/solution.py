
def ghm(file, iss=True):
  hm = []
  nz = []
  sk = []
  for y, l in enumerate(file.readlines()):
    hl = []
    skl = []
    for x, v in enumerate(l.strip()):
      v = int(v) if v != '.' else -1
      hl.append(v)
      if v == 9:
        nz.append((x, y))
        skl.append(set([(x, y)]) if iss else 1)
      else:
        skl.append(set() if iss else 0)
    hm.append(hl)
    sk.append(skl)
  return hm, nz, sk

def ib(pz, gr):
  return (0<=pz[0]<len(gr[0])) and (0<=pz[1]<len(gr))

def ud(a, b):
  if type(a) is int:
    return a+b
  a.update(b)
  return a

def giol(hm, ck, sk, n):
  s = sk[ck[1]][ck[0]]
  for c in [(ck[0]-1, ck[1]),(ck[0]+1, ck[1]),(ck[0], ck[1]-1),(ck[0],ck[1]+1)]:
    if ib(c, hm) and hm[c[1]][c[0]] == n:
      sk[c[1]][c[0]] = ud(sk[c[1]][c[0]], s)
      yield c

def apply(hm, ckz, sk, n, fn):
  nckz = set()
  for ck in ckz:
    for new in fn(hm, ck, sk, n-1):
      nckz.add(new)
  return nckz

def vof(x):
  return x if type(x) == int else len(x)

def p1(file, iss=False):
  hm, ckz, sk = ghm(file, iss)
  at = 9
  while at:
    ckz = apply(hm, ckz, sk, at, giol)
    at -= 1
  print(sum(vof(sk[ck[1]][ck[0]]) for ck in ckz))

def p2(file):
  p1(file, True)

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)