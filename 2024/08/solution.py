
def sum(a, b):
  return tuple(x+y for x, y in zip(a, b))

def diff(a, b):
  return tuple(x-y for x, y in zip(a, b))

def ib(tup, max):
  if tup[0]<0: return False
  if tup[1]<0: return False
  if tup[0]>max[0]: return False
  if tup[1]>max[1]: return False
  return True

def p1(file):
  ae = {}
  an = set()
  mx = 0
  my = 0
  grd = []
  for y, line in enumerate(file.readlines()):
    grd.append(list(line.strip()))
    for x, char in enumerate(line.strip()):
      if char not in ('.', '.'):
        ae[char] = ae.get(char, [])
        ae[char].append((x, y))
      mx = x
    my = y
  print(ae)
  for _, aes in ae.items():
    for x in range(len(aes)):
      for y in range(x+1, len(aes)):
        an1 = aes[x]
        an2 = aes[y]
        up = sum(diff(an1, an2), an1)
        down = sum(diff(an2, an1), an2)
        print('antennae', an1, an2)
        print('antinodes', up, down)
        if ib(up, (mx, my)):
          an.add(up)
        if ib(down, (mx, my)):
          an.add(down)
  for c in an:
    grd[c[1]][c[0]] = '#'
  for l in grd:
    print(l)
  print(len(an))


def p2(file):
  ae = {}
  an = set()
  mx = 0
  my = 0
  grd = []
  for y, line in enumerate(file.readlines()):
    grd.append(list(line.strip()))
    for x, char in enumerate(line.strip()):
      if char not in ('.', '.'):
        ae[char] = ae.get(char, [])
        ae[char].append((x, y))
      mx = x
    my = y
  print(ae)
  coord = (mx, my)
  for _, aes in ae.items():
    for x in range(len(aes)):
      for y in range(x+1, len(aes)):
        an1 = aes[x]
        an2 = aes[y]
        d12 = diff(an1, an2)
        d21 = diff(an2, an1)
        print('antennae', an1, an2)
        while ib(an1, coord):
          an.add(an1)
          an1 = sum(an1, d12)
        while ib(an2, coord):
          an.add(an2)
          an2 = sum(an2, d21)
  for c in an:
    grd[c[1]][c[0]] = '#'
  for l in grd:
    print(l)
  print(len(an))





import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)