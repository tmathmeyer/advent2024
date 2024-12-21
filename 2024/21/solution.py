import functools

def gasimp(x1, y1, x2, y2, bcs):
  if (x1,y1) != bcs:
    if (x1,y1) == (x2,y2):
      yield ''
    if x1 < x2:
      msg = '>'*(x2-x1)
      for cl in gasimp(x2, y1, x2, y2, bcs):
        yield f'{msg}{cl}'
    if x1 > x2:
      msg = '<'*(x1-x2)
      for cl in gasimp(x2, y1, x2, y2, bcs):
        yield f'{msg}{cl}'
    if y1 < y2:
      msg = 'v'*(y2-y1)
      for cl in gasimp(x1, y2, x2, y2, bcs):
        yield f'{msg}{cl}'
    if y1 > y2:
      msg = '^'*(y1-y2)
      for cl in gasimp(x1, y2, x2, y2, bcs):
        yield f'{msg}{cl}'

@functools.cache
def gasimpc(x1, y1, x2, y2, bcs, _):
  return list(gasimp(x1, y1, x2, y2, bcs))


def md(A, B):
  return abs(A[0] - B[0]) + abs(A[1] - B[1])

#789
#456
#123
# 0A
NKCM = {
  '7': (0, 0),
  '8': (1, 0),
  '9': (2, 0),
  '4': (0, 1),
  '5': (1, 1),
  '6': (2, 1),
  '1': (0, 2),
  '2': (1, 2),
  '3': (2, 2),
  '0': (1, 3),
  'A': (2, 3)
}
# ^A
#<v>
DKCM = {
  '^': (1, 0),
  'A': (2, 0),
  '<': (0, 1),
  'v': (1, 1),
  '>': (2, 1),
}


def numpaths(F, T):
  yield from gasimpc(*NKCM[F], *NKCM[T], (0, 3), False)

def dirpaths(F, T):
  yield from gasimpc(*DKCM[F], *DKCM[T], (0, 0), True)

def getseq(seq, func, start='A'):
  if len(seq):
    first, *rest = seq
    seqs = list(getseq(rest, func, first))
    for path in func(start, first):
      for seq in seqs:
        yield f'{path}A{seq}'
  else:
    yield ''

def unpack_all(seqs, func):
  for seq in seqs:
    yield from getseq(seq, func)

@functools.cache
def genseq(seq):
  return list(unpack_all([f'{seq}A'], dirpaths))[0]

@functools.cache
def genlen(seq, d):
  if d == 0:
    return len(seq)+1
  if d < 0:
    raise Exception(f'FUCK {d}')
  return splitcheck(genseq(seq), d)

@functools.cache
def splitcheck(sequence, depth):
  return sum(genlen(c, depth-1) for c in sequence.split('A')[:-1])

def seq2len(seq, depth):
  min = None
  for s in unpack_all([seq], numpaths):
    value = splitcheck(s, depth)
    if min is None or value < min:
      min = value
  return min

def p1(file):
  sum = 0
  for line in file.readlines():
    val = line.strip()
    numeric = int(val[:3])
    minlen = seq2len(val, 3)
    sum += numeric*minlen
  print(sum)

def p2(file):
  sum = 0
  for line in file.readlines():
    val = line.strip()
    numeric = int(val[:3])
    minlen = seq2len(val, 26)
    sum += numeric*minlen
  print(sum)




import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)