S = str(input())
alpha = [0] * 26
num = [0] * 10
for s in S:
  if s.isalpha():
    alpha[ord(s) - ord('A')] += 1
  else:
    num[int(s)] += 1

ans = ""
for i, cnt in enumerate(alpha):
  if cnt > 0:
    ans += ((chr(ord('A') + i) * cnt))

n = 0
for i, cnt in enumerate(num):
  n += (i * cnt)

ans += str(n)
print(ans)