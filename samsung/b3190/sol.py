import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
K = int(input())
graph = [[False]*N for _ in range(N)]
for _ in range(K):
  a, b = map(int, input().split())
  graph[a-1][b-1] = True

L = int(input())
X, C = input().split()
X = int(X)
L -= 1
t = 1

snake = deque([(0, 0)])
dir = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
  hr, hc = snake[0]
  nhr, nhc = hr+dr[dir], hc+dc[dir]
  if nhr < 0 or nhr >= N or nhc < 0 or nhc >= N or (nhr, nhc) in snake: 
    break
  
  snake.appendleft((nhr, nhc))
  if graph[nhr][nhc]:
    graph[nhr][nhc] = False
  else:
    snake.pop()
  
  if X == t:
    if C == "L":
      dir = (dir-1)%4
    elif C == "D":
      dir = (dir+1)%4
    if L > 0:
      X, C = input().split()  
      X = int(X)
      L -= 1
  t += 1
print(t)