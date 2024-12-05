def dx(c, i):
  for x in range(c): yield i[x::c]

def p1():
  with open('input.txt', 'r') as f:
    l,_, _, r = dx(4, sum((x.strip().split(' ') for x in f.readlines()), []))
    print(sum(abs(int(x)-int(y)) for x,y in zip(sorted(l), sorted(r))))

def p2():
  with open('input.txt', 'r') as f:
    l,_, _, r = dx(4, sum((x.strip().split(' ') for x in f.readlines()), []))
    print(sum([r.count(x) * int(x) for x in l]))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
locals()[sys.argv[1]]()