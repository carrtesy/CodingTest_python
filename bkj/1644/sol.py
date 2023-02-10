N = int(input())
primes = [i for i in range(N + 1)]
is_prime = [True for _ in range(N + 1)]
is_prime[0], is_prime[1] = False, False
for i in range(2, N + 1):
  if not is_prime[i]:
    continue
  for j in range(2 * i, N + 1, i):
    is_prime[j] = False
primes = list(filter(lambda x: is_prime[x], primes))

i, j = 0, 0
s, cnt = 0, 0
while True:
  if s < N:
    if j >= len(primes):
      break
    s += primes[j]
    j += 1
  else:
    if s == N:
      cnt += 1
    s -= primes[i]
    i += 1
print(cnt)