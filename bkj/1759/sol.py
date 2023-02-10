from itertools import combinations

L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
for ele in combinations(arr, L):
  v = sum(map(lambda x: x in ['a', 'e', 'i', 'o', 'u'], ele))
  if v >= 1 and L - v >= 2:
    print("".join(list(ele)))
