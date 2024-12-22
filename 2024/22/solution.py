
def next_secret(input):
  input = ((input * 64) ^ input) % 16777216
  input = (int(input // 32) ^ input) % 16777216
  input = ((input * 2048) ^ input) % 16777216
  return input

def get_ones(input):
  while True:
    yield input % 10
    input = next_secret(input)

def get_pcc(input):
  last = None
  for ones in get_ones(input):
    delt = None if last is None else ones - last
    yield ones, delt
    last = ones

def gen4map(input, count):
  seq2price = {}
  pccit = get_pcc(input)
  next(pccit)
  seq = tuple(d for _,(o,d) in zip('...', pccit))
  count -= 4
  for _,(o,d) in zip(range(count), pccit):
    key = tuple([*seq, d])
    if key not in seq2price:
      seq2price[key] = o
    seq = key[1:]
  return seq2price

def seqnum(input, cnt):
  for _ in range(cnt):
    input = next_secret(input)
  return input

def p1(file):
  sum = 0
  for line in file.readlines():
    inp = int(line.strip())
    sum += seqnum(inp, 2000)
  print(sum)

def p2(file):
  scores = {}
  for i,line in enumerate(file.readlines()):
    print(f'Genmap {i}')
    for seq, price in gen4map(int(line.strip()), 2000).items():
      if seq not in scores:
        scores[seq] = 0
      scores[seq] += price
  print(max(scores.values()))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)