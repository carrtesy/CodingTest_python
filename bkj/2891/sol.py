N, S, R = map(int, input().split())
arr = [1] * (N + 1)

for i in list(map(int, input().split())):
  arr[i] -= 1
for i in list(map(int, input().split())):
  arr[i] += 1

if arr[1] == 2 and arr[2] == 0:
  arr[1], arr[2] = 1, 1

for i in range(2, N):
  if arr[i] == 2 and arr[i - 1] == 0:
    arr[i], arr[i - 1] = 1, 1
  if arr[i] == 2 and arr[i + 1] == 0:
    arr[i], arr[i + 1] = 1, 1

if arr[N] == 2 and arr[N - 1] == 0:
  arr[N], arr[N - 1] = 1, 1

cnt = 0
for i in arr:
  if i == 0:
    cnt += 1

print(cnt)
