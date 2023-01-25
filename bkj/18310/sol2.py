import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
idx = N // 2 if N % 2 else N // 2 - 1
best = arr[idx]
print(best)
