N, M = map(int, input().split())
lst = []
dp = [0] * (10001)

for i in range(N):
  coin = int(input())
  lst.append(coin)
  dp[coin] = 1


def mincoin(won):
  if won <= 0:
    return -1
  if dp[won]:
    return dp[won]

  m = 99999
  for coin in lst:
    sub = mincoin(won - coin)
    if sub != -1:
      m = min(m, sub + 1)
  dp[won] = -1 if m == 99999 else m
  return dp[won]


print(mincoin(M))
