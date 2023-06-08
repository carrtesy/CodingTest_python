
N = int(input())


class Student:

  def __init__(self, name, score):
    self.name = name
    self.score = score

  def __repr__(self):
    return self.name

  def __lt__(self, other):
    return self.score < other.score


lst = []
for i in range(N):
  k, v = input().split()
  lst.append(Student(k, int(v)))
lst.sort()
print(lst)
