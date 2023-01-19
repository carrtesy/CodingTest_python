S = str(input())

# input -> segment cnt
arr = []
value = S[0]
tmp = 0
for i in S:
  if i == value:
    tmp += 1
  else:
    arr.append(tmp)
    tmp = 1
    value = i
arr.append(tmp)

# arr reduce
arr = [0] + arr + [0]
cnt = 0
while len(arr) > 3:
  argmax, max_val = -1, -1
  for i in range(1, len(arr) - 1):
    s = arr[i - 1] + arr[i] + arr[i + 1]
    if s > max_val:
      argmax, max_val = i, s
  arr = arr[:argmax - 1] + [max_val] + arr[argmax + 2:]
  cnt += 1
print(cnt)