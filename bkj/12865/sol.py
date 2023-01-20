N, K = map(int, input().split())
arr = [[0] * (K + 1) for i in range(2)]

info = []
for i in range(N):
  w, v = map(int, input().split())
  info.append((w, v))

for i in range(N):
  w, v = info[i]
  for k in range(1, K + 1):
    if w > k:
      arr[1][k] = arr[0][k]
    else:
      arr[1][k] = max(v + arr[0][k - w], arr[0][k])
  arr[0] = arr[1]
  arr[1] = [0] * (K + 1)

print(arr[0][K])