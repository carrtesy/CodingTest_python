N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)

arr.sort()
print(arr)
a, b = arr[-1], arr[-2]

g = M // (K + 1)
r = M % (K + 1)

answer = (K * a + b) * g + a * r
print(answer)
