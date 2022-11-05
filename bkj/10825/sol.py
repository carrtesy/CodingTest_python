import sys

N = int(input())


class Student:

  def __init__(self, name, g, y, s):
    self.name = name
    self.g = g
    self.y = y
    self.s = s

  def __repr__(self):
    return self.name

  def __lt__(self, other):
    if self.g != other.g:
      return self.g > other.g
    else:
      if self.y != other.y:
        return self.y < other.y
      else:
        if self.s != other.s:
          return self.s > other.s
        else:
          return self.name < other.name


students = []
for i in range(N):
  name, g, y, s = sys.stdin.readline().split()
  students.append(Student(name, int(g), int(y), int(s)))

students.sort()
answer = "\n".join([str(x) for x in students])
print(answer)
