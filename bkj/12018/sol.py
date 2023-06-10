import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
  p, l = map(int, input().split())
  row = sorted(list(map(int, input().split())), reverse=True)
  need = row[l-1] if p > l else 1
  arr.append(need)
arr.sort()
T = sum(arr)
ans = len(arr)
while T > m:
  T -= arr[ans-1]
  ans -= 1
print(ans)