
D = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def pg(g):
  for l in g:
    print(''.join([str(c) for c in l]))

def rg(f):
  g = []
  for l in f.readlines():
    g.append(list(l.strip()))
  return g, (len(g[0])-2, 1), (1, len(g)-2)

def gsg(g, e, s):
  sg = [[(-1, '.') for _ in l] for l in g]
  ntc = [s]
  sg[s[1]][s[0]] = (0, '>')
  while ntc:
    nntc = []
    for x,y in ntc:
      sco, dir = sg[y][x]
      for chkdir in '><v^':
        dx, dy = D[chkdir]
        nn = (x+dx, y+dy)
        if g[nn[1]][nn[0]] in '.E':
          sc2n = sco + (1 if chkdir == dir else 1001)
          osco, _ = sg[nn[1]][nn[0]]
          if osco == -1 or sc2n < osco:
            sg[nn[1]][nn[0]] = (sc2n, chkdir)
            nntc.append(nn)
    ntc = nntc
  return sg

def get_cheap_wb_set(sg, e):
  x, y = e
  score, _ = sg[y][x]
  nodex = set([e])
  if score == 0:
    return nodex
  lowest = (score, None)
  for chkdir in '><v^':
    dx, dy = D[chkdir]
    nscore, _ = sg[y+dy][x+dx]
    if nscore != -1:
      if nscore == lowest[0]:
        lowest = (nscore, [chkdir, (x+dx, y+dy)] + lowest[1])
      elif nscore in (score-1, score-1001) and nscore < lowest[0]:
        lowest = (nscore, [(chkdir, (x+dx, y+dy))])

  if lowest[0] == score-1:
    for _, coord in lowest[1]:
      nodex |= get_cheap_wb_set(sg, coord)
    return nodex

  if lowest[0] == score-1001:
    for d, coord in lowest[1]:
      dx,dy = D[d]
      nodex |= get_cheap_wb_set(sg, coord)
      skcore, _ = sg[y+2*dy][x+2*dx]
      if skcore == score - 2:
        nodex |= get_cheap_wb_set(sg, (x+2*dx, y+2*dy))
    return nodex

def p1(file):
  g, e, s = rg(file)
  sg = gsg(g, e, s)
  print(sg[e[1]][e[0]])

def p2(file):
  g, e, s = rg(file)
  sg = gsg(g, e, s)
  print(len(get_cheap_wb_set(sg, e)))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)