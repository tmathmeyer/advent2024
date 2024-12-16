def p1():
  with open('input.txt', 'r') as f:
    grid = [list(x.strip()) for x in f.readlines()]
    pbl = []
    def proc(enz):
      for l, x, y, dx, dy in enz:
        if (0<=x<len(grid[0])) and (0<=y<len(grid)):
          if grid[y][x] == l[0]:
            yield (l[1:],x+dx,y+dy,dx,dy)
    for y in range(len(grid)):
      for x in range(len(grid[0])):
        for z in range(9):
          dy = (z//3)-1
          dx = (z%3)-1
          if dy != 0 or dx != 0:
            pbl.append(('XMAS', y, x, dy, dx))
    print(len(list(proc(proc(proc(proc(pbl)))))))

def p2():
  with open('input.txt', 'r') as f:
    grid = [list(x.strip()) for x in f.readlines()]
    cnt = 0
    for y in range(len(grid)):
      for x in range(len(grid[0])):
        if y in (0, len(grid)-1) or x in (0, len(grid)-1):
          continue
        if grid[y][x] != 'A':
          continue
        if 'M' not in (grid[y-1][x-1], grid[y+1][x+1]):
          continue
        if 'S' not in (grid[y-1][x-1], grid[y+1][x+1]):
          continue
        if 'M' not in (grid[y-1][x+1], grid[y+1][x-1]):
          continue
        if 'S' not in (grid[y-1][x+1], grid[y+1][x-1]):
          continue
        cnt += 1
    print(cnt)



import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
locals()[sys.argv[1]]()