
import networkx as nx

def f2g(file):
  g = nx.Graph()
  for line in file.readlines():
    A, B = line.strip().split('-')
    g.add_edge(A, B)
    g.add_edge(B, A)
  return g

def tct(g):
  for X in g.nodes():
    if X[0] == 't':
      for Y in g.edges(X):
        Y = Y[1]
        for Z in g.edges(Y):
          Z = Z[1]
          if X in [z[1] for z in g.edges(Z)]:
            yield tuple(sorted([X, Y, Z]))

def p1(file):
  g = f2g(file)
  r = set(list(tct(g)))
  print(len(r))

def p2(file):
  g = f2g(file)
  mc = []
  for c in nx.find_cliques(g):
    if len(c) > len(mc):
      mc = c
  print(','.join(sorted(list(mc))))

import sys
if len(sys.argv) != 2:raise Exception('./min.py pNUM')
with open('input.txt') as f:
  locals()[sys.argv[1]](f)