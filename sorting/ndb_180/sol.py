N = int(input())
lst = []
for i in range(N):
  k, v = input().split()
  lst.append((k, int(v)))
lst.sort(key=lambda x:x[1])
print(lst)

