length, target = 10, 7
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# recursive way
def binary_search(arr, s, e, target):
  if s > e:
    return -1
  mid = (s + e) // 2
  v = arr[mid]
  if v < target:
    return binary_search(arr, mid + 1, e, target)
  elif v > target:
    return binary_search(arr, s, mid - 1, target)
  else:
    return mid


print(binary_search(arr, 0, length - 1, target))

# iterative way
s, e, idx = 0, length - 1, -1
while s <= e:
  m = (s + e) // 2
  v = arr[m]
  if v < target:
    s = m + 1
  elif v > target:
    e = m - 1
  else:
    idx = m
    break
print(idx)
