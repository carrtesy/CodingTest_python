import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
  row = list(map(int, input().split()))
  arr.append(row)

def calc(v, arr):
  start = [i for i in range(len(v)) if v[i]==0]
  link = [i for i in range(len(v)) if v[i]==1]
  a = 0
  for i in start:
    for j in start:
      a += arr[i][j]

  b = 0
  for i in link:
    for j in link:
      b += arr[i][j]
  return abs(a-b)

def dfs(v, visited, N):
  if sum(v) == N//2:
    return calc(v, arr)
  
  ans = 9999999
  for i in range(N):
    if v[i] == 0:
      v[i] = 1
      hash = ''.join(map(str, v))
      if hash not in visited:
        ans = min(ans, dfs(v, visited, N))
        visited.add(hash)
      v[i] = 0
  return ans
  
v = [0]*N
visited = set()
print(dfs(v, visited, N))