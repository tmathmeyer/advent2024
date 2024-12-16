
def va(a, b):
  return (a[0]+b[0], a[1]+b[1])

def mul(A, B):
  return tuple(tuple(sum(map(int.__mul__, x, y)) for y in zip(*B)) for x in A)

def oob(pz, gr):
  return not((0<=pz[0]<len(gr[0])) and (0<=pz[1]<len(gr)))

def import_grid(cmap, file):
  with open(file, 'r') as f:
    grid = [list(x.strip()) for x in f.readlines()]
    for y in range(len(grid)):
      for x in range(len(grid)):
        if grid[y][x] in cmap:
          return grid, (x,y), (x,y), cmap[grid[y][x]]

def ng(grid, x, y):
  return [[
    'X' if (x,y)==(En,Rn) else Ev for Ev,En in zip(Rv, range(len(Rv)))
  ] for Rv,Rn in zip(grid,range(len(grid)))]

def p1h(v, grid, pz, mv, DBG=False):
  rm = ((0, 1), (-1, 0))
  vz = set()
  dup = set()
  grid = ng(grid, -1, -1)
  for y in range(len(grid)):
    for x in range(len(grid)):
      if grid[y][x] in v:
        pz = (x, y)
        mv = v[grid[y][x]]
        break
  while True:
    grid[pz[1]][pz[0]] = '$'
    pd = (pz, mv)
    if pd in dup:
      return None
    dup.add(pd)
    vz.add(pz)
    nz = va(mv, pz)
    if oob(nz, grid):
      break
    if grid[nz[1]][nz[0]] in ('#', 'X'):
      mv = mul([mv],rm)
      mv = mv[0]
    else:
      pz = nz
      grid[pz[1]][pz[0]] = 'O'

    if DBG:
      print(len(vz))
      for row in grid:
        print(' '.join(row))
      input('')
  return vz

def p1():
  cmap = {'^':(0,-1),'>':(1,0),'v':(0,1),'<':(-1,0)}
  grid, _, pos, vel = import_grid(cmap, 'input.txt')
  print(len(p1h(cmap, grid, pos, vel)))

def p2():
  cmap = {'^':(0,-1),'>':(1,0),'v':(0,1),'<':(-1,0)}
  grid, start, pos, vel = import_grid(cmap, 'input.txt')
  visited = p1h(cmap, grid, pos, vel)
  loops = 0
  for c,(x,y) in enumerate(visited):
    print(f'{c}/{len(visited)}')
    if (x,y) != start:
      mock_grid = ng(grid, x, y)
      if p1h(cmap, mock_grid, pos, vel) == None:
        loops += 1
  print(loops)

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
locals()[sys.argv[1]]()