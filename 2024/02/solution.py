
def crit(r):
  ok = lambda s,x: (4>abs(x)>0) and s*x>0
  return len(r) == 1 or all(ok(r[0]-r[1], a-b) for a,b in zip(r[:-1], r[1:]))
def dmpn(r):
  return any(crit(r[:x]+r[x+1:]) for x in range(len(r)))
def p1():
  with open('input.txt', 'r') as f:
    print(len([0 for l in f.readlines() if crit([int(x) for x in l.strip().split(' ')])]))
def p2():
  with open('input.txt', 'r') as f:
    print(len([0 for l in f.readlines() if dmpn([int(x) for x in l.strip().split(' ')])]))


import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
locals()[sys.argv[1]]()