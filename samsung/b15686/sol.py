import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
  row = list(map(int, input().split()))
  graph.append(row)

home = []
chicken = []
for r in range(N):
  for c in range(N):
    if graph[r][c] == 1:
      home.append((r, c))
    elif graph[r][c] == 2:
      chicken.append((r, c))

H, C = len(home), len(chicken)
dist = [[0]*C for _ in range(H)]
for h in range(H):
  for c in range(C):
    dist[h][c] = abs(home[h][0]-chicken[c][0]) + abs(home[h][1]-chicken[c][1])

idxes = [i for i in range(len(chicken))]
min_city_dist = 99999
for comb in combinations(idxes, M):
  city_dist = 0
  for h in range(H):
    city_dist+= min(map(lambda c: dist[h][c], comb))
  min_city_dist = min(city_dist, min_city_dist)
print(min_city_dist)