
def XOR(a, b): return a^b
def AND(a, b): return 1 if a and b else 0
def OR(a, b): return 1 if a or b else 0

def f2gm(file):
  values = {}
  l2r = {}
  r2l = {}
  for line in file.readlines():
    if ':' in line:
      w,vs = line.split(': ')
      values[w] = int(vs.strip())
    if '->' in line:
      A,op,B,_,C = line.strip().split(' ')
      r2l[C] = (A, B, globals()[op], {})
      if A not in l2r: l2r[A] = set()
      if B not in l2r: l2r[B] = set()
      l2r[A].add(C)
      l2r[B].add(C)
  return values, l2r, r2l

def bitorder(start, values):
  value = 0
  for k in sorted([k for k in values if k and k[0] == start])[::-1]:
    value <<= 1
    value += values[k]
  return value

def compute(values, l2r, comp):
  r2l = {k:(A,B,op,{}) for k,(A,B,op,_) in comp.items()}
  q = list(values.keys())
  vz = {k:v for k,v in values.items()}
  rendered = set()
  while q:
    w = q.pop(0)
    if w in rendered:
      continue
    for c in l2r.get(w, []):
      r2l[c][3][w] = vz[w]
      if len(r2l[c][3]) == 2:
        vz[c] = r2l[c][2](
          r2l[c][3][r2l[c][0]],
          r2l[c][3][r2l[c][1]])
        q.append(c)
  return vz

def p1(file):
  values, l2r, r2l = f2gm(file)
  print(bitorder('z', compute(values, l2r, r2l)))


def pgv(file):
  values, l2r, r2l = f2gm(file)
  for wire in l2r:
    for end in l2r[wire]:
      print(f'{wire} -> {end}')


def p2(file):
  '''
  Swaps:
  z12, kth
  z26, gsd
  z32, tbt
  qnf, vpm
  '''

  values, l2r, r2l = f2gm(file)
  for value in values:
    values[value] = 0

  o = None
  values[o] = 0
  compute(values, l2r, r2l)
  for x in values:
    values[o] = 0
    o = x
    values[x] = 1
    A = bitorder('x', values)
    B = bitorder('y', values)
    n = compute(values, l2r, r2l)
    C = bitorder('z', n)
    if A + B != C:
      print(f'[change {x}]: {A} + {B} = {C}')

  swaps = ['z12', 'kth', 'z26', 'gsd', 'z32', 'tbt', 'qnf', 'vpm']
  print(','.join(sorted(swaps)))












import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)