import sys
sys.setrecursionlimit(10 ** 6 + 1000)

N = int(input())

memo = [-1] * (N+1)
backtrack = [-1] * (N+1)
memo[1] = 0
backtrack[1] = 1

def dfs(n):
  if memo[n] >= 0:
    return memo[n]

  ans = int(1e9)
  
  if n % 3 == 0:
    subans = dfs(n//3)+1
    if ans > subans:
      ans = subans
      backtrack[n] = n//3
  
  if n % 2 == 0:
    subans = dfs(n//2)+1
    if ans > subans:
      ans = subans
      backtrack[n] = n//2
  
  subans = dfs(n-1)+1
  if ans > subans:
    ans = subans
    backtrack[n] = n-1
  
  memo[n] = ans
  return memo[n]

print(dfs(N))
while N != 1:
  print(N, end=" ")
  N = backtrack[N]
print("1")