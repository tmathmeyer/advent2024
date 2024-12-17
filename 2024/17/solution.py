
def rf(file):
  registers = {}
  for line in file.readlines():
    line = line.strip()
    if line.startswith('Register'):
      registers[line[9]] = int(line[12:])
    if line.startswith('Program'):
      return [int(x) for x in line[9:].split(',')], registers

class Comp():
  def __init__(self, file):
    self._tape, self._reg = rf(file)
    self._ip = 0
    self._output = []

  def _opval(self, covid):
    if covid in (4, 5, 6):
      return self._reg['....ABC'[covid]]
    return covid

  def tick(self):
    if self._ip >= len(self._tape):
      return False
    opcode, operand = self._tape[self._ip], self._tape[self._ip+1]
    jump = self._ip + 2
    if opcode == 0:
      self._reg['A'] = int(self._reg['A'] / (2**self._opval(operand)))
    if opcode == 1:
      self._reg['B'] = self._reg['B'] ^ operand
    if opcode == 2:
      self._reg['B'] = self._opval(operand) % 8
    if opcode == 3:
      if self._reg['A']:
        jump = operand
    if opcode == 4:
      self._reg['B'] = self._reg['B'] ^ self._reg['C']
    if opcode == 5:
      self._output.append(str(self._opval(operand) % 8))
    if opcode == 6:
      self._reg['B'] = int(self._reg['A'] / (2**self._opval(operand)))
    if opcode == 7:
      self._reg['C'] = int(self._reg['A'] / (2**self._opval(operand)))
    self._ip = jump
    return True

  def ds(self):
    print(self._reg, self._tape, self._ip)

def p1(file):
  c = Comp(file)
  while True:
    if c.tick():
      continue
    break
  print(','.join(c._output))

def checktape(x, exp):
  A, B, C = x, 0, 0
  B = A % 8
  B = B ^ 5
  C = int(A / (2**B))
  B = B ^ 6
  B = B ^ C
  return B % 8 == exp

def get_ok_as(stream, exp):
  for x in stream:
    if checktape(x, exp):
      yield x

def expl(stream):
  for x in stream:
    for i in range(8):
      yield x*8 + i

def p2(file):
  c = Comp(file)
  rtape = c._tape[::-1]
  stream = range(100)
  filter = []
  for c in rtape:
    filter = get_ok_as(stream, c)
    stream = expl(filter)
  print(next(filter))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)