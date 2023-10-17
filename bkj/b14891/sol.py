import sys
from collections import deque
input = sys.stdin.readline

arr = [[]]
for _ in range(4):
  row = deque(map(int, list(input().strip())))
  arr.append(row)

L, R = 6, 2

K = int(input())
while K:
  K -= 1
  N, D = map(int, input().split())
  
  rt = [0] * 5
  rt[N] = D
  
  for i in range(N, 4):
    if arr[i][R] != arr[i+1][L]:
      D *= -1
      rt[i+1] = D
    else:
      break

  D = rt[N]
  for i in range(N, 1, -1):
    if arr[i][L] != arr[i-1][R]:
      D *= -1
      rt[i-1] = D
    else:
      break
      
  for i in range(1, 5):
    arr[i].rotate(rt[i])

print(arr[1][0]+2*arr[2][0]+4*arr[3][0]+8*arr[4][0])