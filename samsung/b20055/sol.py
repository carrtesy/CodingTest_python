import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
UP, DOWN = 0, N-1
arr = deque(list(map(int, input().split())))
robots = []
cnt = 1

while True:  
  # 1
  arr.rotate()
  robots = [(r+1)%(2*N) for r in robots if (r+1) != DOWN]

  # 2
  for i in range(len(robots)):
    next_pos = (robots[i]+1)%(2*N)
    if robots[i] != -1 and arr[next_pos] > 0 and (next_pos not in robots):
      robots[i] = next_pos
      arr[next_pos] -= 1
      if next_pos == DOWN:
        robots[i] = -1   
  robots = [r for r in robots if r!=-1]

  # 3
  if arr[UP] > 0:
    robots.append(0)
    arr[0] -= 1
  
  # 4
  if sum([a<=0 for a in arr]) >= K:
    break
  cnt += 1
  
print(cnt)