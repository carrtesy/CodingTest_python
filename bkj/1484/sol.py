G = int(input())

result = []
j = G+1
for i in range(1, G+1):
  if G % i == 0:
    j = G // i
    if i >= j:
      break  
    if (i+j)%2 == 0:
      result.insert(0, (i+j)//2)

if len(result) > 0:
  print("\n".join(map(str, result)))
else:
  print(-1)