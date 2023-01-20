N = int(input())


class st:

  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

  def __lt__(self, a):
    return self.grade < a.grade


l = []
for i in range(N):
  name, grade = input().split()
  name, grade = str(name), int(grade)
  l.append(st(name, grade))

l.sort()
for i in l:
  print(i.name)
print(l)
