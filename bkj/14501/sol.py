N = int(input())
T, P = [], []

for i in range(N):
  Ti, Pi = map(int, input().split())
  T.append(Ti)
  P.append(Pi)

dp = [-1] * N


def search(N, T, P, d):

  if d >= N:
    return 0
  pay = 0
  if dp[d] == -1:
    # do
    if d + T[d] <= N:
      do = P[d] + search(N, T, P, d + T[d])
      pay = max(do, pay)
    # not
    if d + 1 <= N:
      dont = search(N, T, P, d + 1)
      pay = max(dont, pay)
    dp[d] = pay
  return dp[d]


print(search(N, T, P, 0))
