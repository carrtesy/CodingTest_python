import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().split())

r,c = 1, 1
for m in arr:
    if m == "R":
        c = min(c+1, N)
    elif m == "U":
        r = max(r-1, 1)
    elif m == "D":
        r = min(r+1, N)
    elif m == "L":
        c = max(c-1, 1)
print(r, c)