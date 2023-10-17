import sys
N, M, K = map(int,input().split())
print(N, M, K)

arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr)

s = 0
a, b = M//K, M%K

for i in range(a):
    s += (arr[i]*K)
s += (arr[a+1]*b)
print(s)