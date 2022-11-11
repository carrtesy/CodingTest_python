X = int(input())
dp = [-1] * 30001
dp[0], dp[1] = 0, 0

cnt = 0


def find(X):
  if dp[X] != -1:
    return dp[X]

  m = find(X - 1) + 1
  if X % 5 == 0:
    m = min(m, find(X // 5) + 1)
  if X % 3 == 0:
    m = min(m, find(X // 3) + 1)
  if X % 2 == 0:
    m = min(m, find(X // 2) + 1)

  dp[X] = m
  return m


print(find(X))
print(cnt)
