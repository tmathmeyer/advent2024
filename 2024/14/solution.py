
def rf(f):
  for l in f.readlines():
    p,v = l.strip().split(' ')
    px,py = p[2:].split(',')
    dx,dy = v[2:].split(',')
    yield (int(px), int(py)), (int(dx), int(dy))


def p1(file):
  grid = (101, 103)
  s = 100
  qds = [0, 0, 0, 0]
  pos = {}

  for rp, rv in rf(file):
    nx = rp[0] + s*rv[0]
    ny = rp[1] + s*rv[1]
    np = ( nx%(grid[0]), ny%(grid[1]) )
    if np in pos:
      pos[np] += 1
    else:
      pos[np] = 1
    if np[0] < int(grid[0]//2):
      if np[1] < int(grid[1]//2):
        qds[0] += 1
      elif np[1] > int(grid[1]//2):
        qds[1] += 1
    elif np[0] > int(grid[0]//2):
      if np[1] < int(grid[1]//2):
        qds[2] += 1
      elif np[1] > int(grid[1]//2):
        qds[3] += 1
  mul = 1
  for x in qds:
    mul *= x
  print(mul)


def p2(file):
  grid = (101, 103)
  robots = list(rf(file))
  for n in range(100):
    pos = {}
    s = 11 + 101*n
    for rp, rv in robots:
      nx = rp[0] + s*rv[0]
      ny = rp[1] + s*rv[1]
      np = ( nx%(grid[0]), ny%(grid[1]) )
      if np in pos:
        pos[np] += 1
      else:
        pos[np] = 1
    print(s)
    for y in range(grid[1]):
      print(''.join(str(pos.get((x,y), '.')) for x in range(grid[0])))



import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)