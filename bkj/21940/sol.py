import sys
input = sys.stdin.readline
N, M = map(int, input().split())
INF = int(2*10**5+1)
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
  A, B, T = map(int, input().split())
  graph[A][B] = T
for i in range(1, N+1):
  graph[i][i] = 0

K = int(input())
arr = list(map(int, input().split()))

for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

cities = []
min_dist = INF*10
for city in range(1, N+1):
  dist = max(map(lambda x:graph[x][city]+graph[city][x], arr))
  if dist < min_dist:
    cities, min_dist = [city], dist
  elif dist == min_dist:
    cities.append(city)
print(' '.join(map(str, cities)))
    
    