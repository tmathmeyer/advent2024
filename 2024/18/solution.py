

D = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def av(a, b):
  return (a[0]+b[0], a[1]+b[1])

def ib(pz, gr):
  return (0<=pz[0]<len(gr[0])) and (0<=pz[1]<len(gr))

def rf(file):
  for l in file.readlines():
    yield (int(x) for x in l.strip().split(','))

def rf2g(file, gs, ls):
  g = [['.' for _ in range(gs)] for _ in range(gs)]
  it = rf(file)
  for _ in range(ls):
    x,y = next(it)
    g[y][x] = '#'
  return g, it

def cg(g):
  return [[x for x in l] for l in g]

def bfs(g, sx, sy, ex, ey):
  g[sx][sy] = 0
  cn = set([(sx, sy)])
  while cn:
    nn = set()
    for c in cn:
      #print(f'Checking {c=}')
      cv = g[c[1]][c[0]]
      for d in '^v<>':
        cp = av(D[d], c)
        if ib(cp, g):
          cpv = g[cp[1]][cp[0]]
          if cpv == '.':
            g[cp[1]][cp[0]] = cv+1
            nn.add(cp)
          elif cpv != '#' and cpv > cv:
            g[cp[1]][cp[0]] = cv+1
            nn.add(cp)
    cn = nn

def mpb(l):
  for x in l:
    if type(x) is str:
      yield x
    else:
      yield str(x)

def pg(grid):
  for x in grid:
    print(' '.join(mpb(x)))

def a2g(g, f, D):
  for x,y in f:
    g[y][x] = '#'
  cop = cg(g)
  bfs(cop, 0, 0, D-1, D-1)
  return cop[D-1][D-1]

def p0(file):
  D = 7
  grid, _ = rf2g(file, D, 12)
  bfs(grid, 0, 0, D-1, D-1)
  print(grid[D-1][D-1])

def p1(file):
  D = 71
  grid, _ = rf2g(file, D, 1024)
  bfs(grid, 0, 0, D-1, D-1)
  print(grid[D-1][D-1])

def p2(file):
  D = 71
  grid, it = rf2g(file, D, 1024)
  rem = [(x,y) for x,y in it]

  for x in range(1900, len(rem)):
    rs = rem[0:x]
    if a2g(grid, rs, D) == '.':
      print(rs[-1])
      return

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)