import sys

input = sys.stdin.readline
while True:
  a, b, c = tuple(sorted(list(map(int, input().split()))))
  if (a == 0) and (b == 0) and (c == 0):
    break
  if a == b and b == c:
    print("Equilateral")
  else:
    if a + b <= c:
      print("Invalid")
    else:
      if a == b or b == c:
        print("Isosceles")
      else:
        print("Scalene")
