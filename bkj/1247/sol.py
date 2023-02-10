import sys
from collections import deque

input = sys.stdin.readline

T = 3
while T:
  T -= 1
  N = int(input())

  pos, neg = [], []
  for _ in range(N):
    n = int(input())
    if n > 0:
      pos.append(n)
    elif n < 0:
      neg.append(n)

  pos = deque(pos)
  neg = deque(neg)

  while pos and neg:
    a, b = pos[0], neg[0]
    if abs(a) > abs(b):
      p = neg.popleft()
      pos[0] = a + b
    elif abs(a) < abs(b):
      p = pos.popleft()
      neg[0] = a + b
    else:
      pos.popleft()
      neg.popleft()

  if pos:
    print('+')
  elif neg:
    print("-")
  else:
    print("0")
