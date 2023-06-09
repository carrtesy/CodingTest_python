X, Y, W, S = map(int, input().split())

if W*2 < S:
  print((X+Y)*W)
else:
  if W < S:
    print(min(X, Y)*S + abs(X-Y) * W)
  else:
    print(min(X, Y)*S + 2*(abs(X-Y) // 2) * S + (abs(X-Y) % 2) * W)