
D = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def av(a, b):
  return (a[0]+b[0], a[1]+b[1])

def ib(pz, gr):
  return (0<=pz[0]<len(gr[0])) and (0<=pz[1]<len(gr))

def cg(g):
  return [[x for x in l] for l in g]

def rg(f):
  mem = {}
  grid = []
  for y,l in enumerate(f.readlines()):
    for x,c in enumerate(l.strip()):
      if c in 'SE':
        mem[c] = (x,y)
    grid.append(list(l.strip()))
  return grid, mem['S'], mem['E']

def mpb(l):
  for x in l:
    if type(x) is str:
      yield x
    else:
      yield str(x%10)

def pg(grid):
  for x in grid:
    print(''.join(mpb(x)))

def bfs(g, sx, sy, path='.', wall='#', max=None):
  g[sy][sx] = 0
  cn = set([(sx, sy)])
  tggd = {(sx, sy): 0}
  while cn:
    nn = set()
    for c in cn:
      cv = g[c[1]][c[0]]
      for d in '^v<>':
        cp = av(D[d], c)
        if ib(cp, g):
          cpv = g[cp[1]][cp[0]]
          if cpv == 'E':
            if wall == '#':
              tggd[cp] = g[cp[1]][cp[0]] = cv+1
              if max is None or cv+1 < max:
                nn.add(cp)
          elif cpv == 'S':
            pass
          elif cpv == path:
            tggd[cp] = g[cp[1]][cp[0]] = cv+1
            if max is None or cv+1 < max:
              nn.add(cp)
          elif cpv != wall and cpv > cv:
            tggd[cp] = g[cp[1]][cp[0]] = cv+1
            if max is None or cv+1 < max:
              nn.add(cp)
    cn = nn
  return tggd

def fscs(g, sx, sy, ex, ey, gt):
  cuts = {}
  while (sx, sy) != (ex, ey):
    nx, ny = ex, ey
    v = g[sy][sx]
    for d in '^v<>':
      n = av(D[d], (sx, sy))
      nv = g[n[1]][n[0]]
      if nv == v+1:
        nx,ny = n
      elif nv == '#':
        sk = av(D[d], n)
        if ib(sk, g):
          sv = g[sk[1]][sk[0]]
          if sv != '#' and sv > v:
            sco = (sv - v) - 2
            if sco not in cuts:
              cuts[sco] = 1
            else:
              cuts[sco] += 1
    sx,sy = nx,ny

  count = 0
  for sco, cnt in cuts.items():
    if sco >= 100:
      count += cnt
  return count


def fscs3(og, g, coord2score, gt=50):
  counts = {}
  for s in coord2score.keys():
    for e in coord2score.keys():
      if s == e: continue
      cop = cg(og)
      cop[s[1]][s[0]] = '#'
      cop[e[1]][e[0]] = '#'
      bfs(cop, *s, path='#', wall='.', max=20)
      endval = cop[e[1]][e[0]]
      if type(endval) is int:
        withshortcut = g[s[1]][s[0]] + endval
        withoutcut = g[e[1]][e[0]]
        if withshortcut < withoutcut:
          savings = withoutcut - withshortcut
          if savings >= gt:
            counts[savings] = counts.get(savings, 0) + 1
  sum = 0
  for x in sorted(counts.keys()):
    print(f'{counts[x]} : {x}')
    sum += counts[x]
  return sum


def fscs2(g, coord2score, gt=50):
  counts = {}
  for s in coord2score.keys():
    for e in coord2score.keys():
      if s == e: continue
      cheatdist = abs(s[0] - e[0]) + abs(s[1] - e[1])
      if cheatdist <= 20:
        withshortcut = g[s[1]][s[0]] + cheatdist
        withoutcut = g[e[1]][e[0]]
        if withshortcut < withoutcut:
          savings = withoutcut - withshortcut
          if savings >= gt:
            counts[savings] = counts.get(savings, 0) + 1
  sum = 0
  for x in sorted(counts.keys()):
    print(f'{counts[x]} : {x}')
    sum += counts[x]
  return sum


def p1(file):
  g, S, E = rg(file)
  bfs(g, *S)
  count = fscs(g, *S, *E, 100)
  print(count)

def p2(file):
  g, S, _ = rg(file)
  coordscore = bfs(g, *S)
  count = fscs2(g, coordscore, 100)
  print(count)

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)