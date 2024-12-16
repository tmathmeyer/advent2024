
def p1s(tot, seq, cc=False):
  if len(seq) == 0:
    return False
  if len(seq) == 1:
    return tot == seq[0]
  f, *r = seq
  if tot % f == 0:
    if p1s(int(tot/f), r, cc):
      return True
  if tot >= f:
    if cc:
      fl = -len(str(f))
      tots = str(tot)
      if tots[fl:] == str(f) and tot != f:
        if p1s(int(tots[:fl]), r, cc):
          return True
    if p1s(tot-f, r, cc):
      return True
  return False

def p1(file, cc=False):
  with open(file, 'r') as f:
    sum = 0
    for x in f.readlines():
      tot_s, vz_s = x.split(':')
      tot = int(tot_s.strip())
      vz = [int(x.strip()) for x in vz_s.strip().split(' ')]
      if p1s(tot, vz[::-1], cc):
        sum += tot
    print(sum)

def p2(file):
  p1(file, cc=True)

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
locals()[sys.argv[1]]('input.txt')