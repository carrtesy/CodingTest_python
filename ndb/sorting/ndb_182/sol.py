N, K = map(int, input().split())
lst1 = sorted(list(map(int, input().split())))
lst2 = sorted(list(map(int, input().split())), reverse=True)

print(lst1)
print(lst2)

for i in range(K):
  if lst1[i] < lst2[i]:
    lst1[i], lst2[i] = lst2[i], lst1[i]
  else:
    break

print(sum(lst1))