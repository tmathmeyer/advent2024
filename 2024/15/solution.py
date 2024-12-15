
D = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def ib(pz, gr):
  return (0<=pz[0]<len(gr[0])) and (0<=pz[1]<len(gr))

def va(a, b):
  return tuple(x+y for x,y in zip(a, b))

def gps(g):
  sum = 0
  for y, l in enumerate(g):
    for x, v in enumerate(l):
      if v in ('O', '['):
        sum += (100*y + x)
  return sum

def dblr(l):
  for c in l:
    if c == 'O':
      yield '['
      yield ']'
    if c == '#':
      yield '#'
      yield '#'
    if c == '.':
      yield '.'
      yield '.'
    if c == '@':
      yield '@'
      yield '.'

def cplr(l):
  yield from l

def rf(f, fn):
  grid = []
  mt = False
  robo = (0, 0)
  steps = []
  for y, l in enumerate(f.readlines()):
    if not l.strip():
      mt = True
    elif not mt:
      grid.append(list(fn(l.strip())))
      if '@' in l:
        v = ''.join(grid[-1])
        robo = (v.index('@'), y)
    else:
      steps += list(l.strip())
  return robo, grid, steps

def cm(g, r, d):
  while ib(r, g):
    if g[r[1]][r[0]] == '.':
      return True
    if g[r[1]][r[0]] == '#':
      return False
    r = va(r, d)
  return False

def camv(g, rs, d):
  acs = []
  if type(rs) != list:
    rs = [rs]
  for c in [va(r, d) for r in rs]:
    if not ib(c, g): return False
    if g[c[1]][c[0]] == '#': return False
    if g[c[1]][c[0]] == '[':
      acs.append(c)
      acs.append((c[0]+1, c[1]))
    if g[c[1]][c[0]] == ']':
      acs.append(c)
      acs.append((c[0]-1, c[1]))
    if g[c[1]][c[0]] == 'O':
      acs.append(c)
  if acs:
    return camv(g, acs, d)
  return True

def mv(g, C, R, d):
  V = g[C[1]][C[0]]
  g[C[1]][C[0]] = R
  N = va(C, d)
  E = g[N[1]][N[0]]
  if E == '[':
    mv(g, N, V, d)
    mv(g, va(N, (1,0)), '.', d)
  if E == ']':
    mv(g, N, V, d)
    mv(g, va(N, (-1,0)), '.', d)
  if E == 'O':
    mv(g, N, V, d)
  if E == '.':
    g[N[1]][N[0]] = V

def mh(g, C, R, d):
  V = g[C[1]][C[0]]
  g[C[1]][C[0]] = R
  N = va(C, d)
  E = g[N[1]][N[0]]
  if E in '[]O':
    mh(g, N, V, d)
  if E == '.':
    g[N[1]][N[0]] = V

def move(g, r, m, d):
  check = cm
  move = mh
  if m in ('v', '^'):
    check = camv
    move = mv
  if check(g, r, d):
    move(g, r, '.', d)
    return va(r, d)
  return r

def p2(file):
  r, g, ms = rf(file, dblr)
  for m in ms:
    r = move(g, r, m, D[m])
  print(gps(g))

def p1(file):
  r, g, ms = rf(file, cplr)
  for m in ms:
    r = move(g, r, m, D[m])
  print(gps(g))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)