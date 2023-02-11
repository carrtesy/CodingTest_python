H, W, N, M = map(int, input().split())
a = W // (1 + N) + int((W % (1 + N)) > 0)
b = H // (1 + M) + int((H % (1 + M)) > 0)
print(a * b)