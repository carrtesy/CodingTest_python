import sys
input = sys.stdin.readline
N = input()
num = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

def eval(num, op):
  result = num[0]
  for i in range(len(op)):
    v = num[i+1]
    if op[i] == '+':
      result += v
    elif op[i] == '-':
      result -= v
    elif op[i] == 'x':
      result *= v
    elif op[i] == '/':
      if result >= 0:
        result //= v
      else:
        result = -(-result // v)
  return result

def dfs(op, a, b, c, d, num, mode="min"):
  if a+b+c+d == 0:
    return eval(num, op)
  result = int(-1e9-1) if mode=="max" else int(1e9+1)
  fn = max if mode=="max" else min
  
  if a:
    result = fn(result, dfs(op+'+', a-1, b, c, d, num, mode))
  if b:
    result = fn(result, dfs(op+'-', a, b-1, c, d, num, mode))
  if c:
    result = fn(result, dfs(op+'x', a, b, c-1, d, num, mode))
  if d:
    result = fn(result, dfs(op+'/', a, b, c, d-1, num, mode))
  return result


print(dfs('', a, b, c, d, num, "max"))
print(dfs('', a, b, c, d, num, "min"))