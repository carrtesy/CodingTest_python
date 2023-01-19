N = str(input())
l = len(N)
f = sum(map(lambda x: int(x), N[:l // 2]))
b = sum(map(lambda x: int(x), N[l // 2:]))
if f == b:
  print("LUCKY")
else:
  print("READY")
