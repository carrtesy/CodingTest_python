num = [int(x) for x in str(input())]

for i in range(len(num) - 1):
  a, b = num[i], num[i + 1]
  num[i + 1] = max(a + b, a * b)

print(num[-1])
