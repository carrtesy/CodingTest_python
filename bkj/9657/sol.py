N = int(input())

mem = [-1] * (N+1)
mem[1] = mem[3] = mem[4] = True
def dfs(n):
  if n < 1:
    return False
  if mem[n] != -1:
    return mem[n]
  mem[n] = dfs(n-1) or dfs(n-3) or dfs(n-4)
  return mem[n]

if dfs(N):
  print("SK")
else:
  print("CY")

print(mem)