n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data = sorted(data)

answer = 0

first = data[-1]
second = data[-2]

cnt = m // (k + 1) + m % (k + 1)
answer += cnt * first
answer += (m - cnt) * second
print(answer)