#import sys
#input = sys.stdin.readline

import sys

sys.stdin = open("input1.txt", "r")
T = int(input())


def swap(arr, i, j):
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp


def dfs(arr, cnt, total, mem):
  l = len(arr)
  ans = 0

  status = int(''.join(arr))
  if (status, cnt) in mem:
    return mem[(status, cnt)]
  if cnt == total:
    return status

  for i in range(l):
    for j in range(i + 1, l):
      swap(arr, i, j)
      ans = max(ans, dfs(arr, cnt + 1, total, mem))
      swap(arr, i, j)
  mem[(status, cnt)] = ans
  return mem[(status, cnt)]


for test_case in range(1, T + 1):
  arr, total = input().split()
  arr, total = list(arr), int(total)
  mem = dict()
  print(f"#{test_case} {dfs(arr, 0, total, mem)}")
