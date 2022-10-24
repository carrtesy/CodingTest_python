N, M = map(int, input().split())
print(N, M)

lst = []
MAX = 0
for i in range(N):
  row = list(map(int, input().split()))
  _MAX = min(row)
  MAX = _MAX if _MAX > MAX else MAX
print(MAX)