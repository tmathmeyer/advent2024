
def rf(file):
  registers = {}
  for line in file.readlines():
    line = line.strip()
    if line.startswith('Register'):
      registers[line[9]] = int(line[12:])
    if line.startswith('Program'):
      return [int(x) for x in line[9:].split(',')], registers

class Comp():
  @staticmethod
  def New(file):
    return Comp(*rf(file))

  def __init__(self, tape, reg):
    self._tape, self._reg = tape, reg
    self._ip, self._output, self._jumps = 0, [], 0

  def Copy(self):
    return Comp(self._tape, self._reg)

  def _opval(self, covid):
    if covid in (4, 5, 6):
      return self._reg['....ABC'[covid]]
    return covid

  def tick(self):
    if self._ip >= len(self._tape):
      return False
    opcode, operand = self._tape[self._ip], self._tape[self._ip+1]
    jump = self._ip + 2
    jumps = 0
    if opcode == 0:
      self._reg['A'] = int(self._reg['A'] / (2**self._opval(operand)))
    if opcode == 1:
      self._reg['B'] = self._reg['B'] ^ operand
    if opcode == 2:
      self._reg['B'] = self._opval(operand) % 8
    if opcode == 3:
      if self._reg['A']:
        jump = operand
        jumps = 1
    if opcode == 4:
      self._reg['B'] = self._reg['B'] ^ self._reg['C']
    if opcode == 5:
      self._output.append(str(self._opval(operand) % 8))
    if opcode == 6:
      self._reg['B'] = int(self._reg['A'] / (2**self._opval(operand)))
    if opcode == 7:
      self._reg['C'] = int(self._reg['A'] / (2**self._opval(operand)))
    self._ip = jump
    self._jumps += jumps
    return True

  def gen_checktape(self):
    def check(x, exp):
      cop = self.Copy()
      cop._reg['A'] = x
      while not cop._jumps:
        if not cop.tick():
          break
      return int(cop._output[0]) == exp
    return check

def checkstream(stream, exp, gct):
  for x in stream:
    if gct(x, exp):
      yield x

def expl(stream, size):
  for x in stream:
    for i in range(size):
      yield x*size + i

def p1(file):
  c = Comp.New(file)
  while True:
    if c.tick():
      continue
    break
  print(','.join(c._output))

def p2(file):
  c = Comp.New(file)
  stream = range(10)
  gct = c.gen_checktape()
  for c in c._tape[::-1]:
    filter = checkstream(stream, c, gct)
    stream = expl(filter, 8)
  print(next(filter))


import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)