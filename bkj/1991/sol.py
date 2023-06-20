import sys
input = sys.stdin.readline

N = int(input())

class Node:
  def __init__(self, name, left=None, right=None):
    self.name = name
    self.left = left
    self.right = right

nodes = [Node(chr(ord('A')+i)) for i in range(N)]

for _ in range(N):
  row = input().strip().split()
  root = ord(row[0]) - ord('A')
  lch, rch = ord(row[1]) - ord('A'), ord(row[2]) - ord('A')
  nodes[root].left = nodes[lch] if row[1] != '.' else None
  nodes[root].right = nodes[rch] if row[2] != '.' else None

def preorder(root):
  print(root.name, end="")
  if root.left: preorder(root.left)
  if root.right: preorder(root.right)

def inorder(root):
  if root.left: inorder(root.left)
  print(root.name, end="")
  if root.right: inorder(root.right)

def postorder(root):
  if root.left: postorder(root.left)
  if root.right: postorder(root.right)
  print(root.name, end="")

preorder(nodes[0])
print()
inorder(nodes[0])
print()
postorder(nodes[0])
print()
