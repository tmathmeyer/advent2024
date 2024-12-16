
def p1(file):
  sizes = [int(x) for x in f.readline()]
  if len(sizes) % 2 != 1:
    sizes = sizes[:-1]
  chk = 0
  tff = True
  index = 0
  sv = 0
  ev = int(len(sizes) // 2)
  mem = []
  while sizes:
    print(f'{chk=}, {sv=}, {ev=}, {index=}')
    if tff:
      if sizes[0] == 0:
        sizes = sizes[1:]
        tff = False
        sv += 1
      else:
        sizes[0] -= 1
        chk += (index * sv)
        mem.append(sv)
        index += 1
    else:
      if sizes[-1] == 0:
        sizes = sizes[:-2]
        ev -= 1
      elif sizes[0] == 0:
        tff = True
        sizes = sizes[1:]
      else:
        sizes[-1] -= 1
        sizes[0] -= 1
        chk += (index * ev)
        mem.append(ev)
        index += 1
  print(chk)

def ss2mem(sizes):
  return sum(([int(i//2) if i%2==0 else '.']*c for i,c in enumerate(sizes)), [])

def flo(ops, bs):
  for i, (idx, s) in enumerate(ops):
    if s >= bs:
      return (i, idx, s)
  return None, None, None

def p2(file):
  sizes = [int(x) for x in f.readline()]
  mem = ss2mem(sizes)
  openings = []
  fillings = []
  idx = 0
  for i, s in enumerate(sizes):
    if i%2==1:
      openings.append((idx, s))
    else:
      fillings.append((idx, s, int(i//2)))
    idx += s

  for (f_idx, f_sz, value) in fillings[::-1]:
    print(value)
    (os, idx, sz) = flo(openings, f_sz)
    if os != None and idx<f_idx:
      for i in range(f_sz):
        mem[idx+i] = value
        mem[f_idx+i] = '.'
      openings[os] = (idx+f_sz, sz-f_sz)

  chk = 0
  for i,v in enumerate(mem):
    if v != '.':
      chk += (i*v)
  print(chk)


import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)