n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data = sorted(data)

answer = 0

first = data[-1]
second = data[-2]

print(first, second)
s = (k * first + second)
q = (m // (k + 1))

print(s, q)
answer += s * q

answer += (m - q * (k + 1)) * first

print(answer)
