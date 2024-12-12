
def rg(f):
  return [[c for c in l.strip()] for l in f.readlines()]

def ib(pz, gr):
  return (0<=pz[0]<len(gr[0])) and (0<=pz[1]<len(gr))

def calc_cost(grid, coord, c):
  area = 0
  perm = 0
  coords = [coord]
  while coords:
    x,y = coords.pop()
    if grid[y][x] != c:
      continue
    area += 1
    grid[y][x] = grid[y][x].lower()
    for cc in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
      if not ib(cc, grid):
        perm += 1
      elif grid[cc[1]][cc[0]] == c:
        coords.append(cc)
      elif grid[cc[1]][cc[0]] not in (c, c.lower()):
        perm += 1
  return area * perm

def dcog(arr):
  dc = 0
  prev = -2
  for v in sorted(arr):
    if v != prev+1: dc += 1
    prev = v
  return dc

def csc(p):
  sc = 0
  for l, cz in p.items():
    a2b = {}
    for x,y in cz:
      if l in ('u','d'): x,y=y,x
      if x not in a2b: a2b[x] = [y]
      else: a2b[x].append(y)
    sc += sum(dcog(y) for y in a2b.values())
  return sc

def calc_cost_a(grid, coord, c):
  area = 0
  permz = {'u':set(), 'd':set(), 'r': set(), 'l':set()}
  coords = [coord]
  while coords:
    x,y = coords.pop()
    if grid[y][x] != c:
      continue
    area += 1
    grid[y][x] = grid[y][x].lower()
    for a,b,d in ((x+1,y,'r'), (x-1,y,'l'), (x,y+1,'d'), (x,y-1,'u')):
      cc = (a,b)
      if not ib(cc, grid):
        permz[d].add((x,y))
      elif grid[cc[1]][cc[0]] == c:
        coords.append(cc)
      elif grid[cc[1]][cc[0]] not in (c, c.lower()):
        permz[d].add((x,y))
  return area * csc(permz)

def p1(file, func=calc_cost):
  grid = rg(file)
  sum = 0
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x].isupper():
        sum += func(grid, (x, y), grid[y][x])
  print(sum)

def p2(file):
  p1(file, calc_cost_a)



import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)