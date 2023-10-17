import sys; input=sys.stdin.readline
from collections import deque

N, Q = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))


def rotate(arr, l):
    if l ==0:
        return arr
    arr_new = [[-1]*(2**N) for _ in range(2**N)]
    for r in range(0, 2**N, 2**l):
        for c in range(0, 2**N, 2**l):
            for dr in range(0, 2**l):
                for dc in range(0, 2**l):
                    arr_new[r+dc][c+(2**l)-dr-1] = arr[r+dr][c+dc]
    return arr_new


def melt(arr):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    arr_new = [[-1]*(2**N) for _ in range(2**N)]

    for r in range(0, 2**N):
        for c in range(0, 2**N):
            cnt = 0
            for i in range(4):
                rp, cp = r+dr[i], c+dc[i]
                if 0<=rp<2**N and 0<=cp<2**N and arr[rp][cp]>0:
                    cnt+=1
            if cnt < 3:
                arr_new[r][c] = max(0, arr[r][c]-1)
            else:
                arr_new[r][c] = arr[r][c]
    return arr_new


def bfs(arr, check, r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = deque([(r, c)])
    check[r][c] = True
    answer = 0

    while queue:
        _r, _c = queue.popleft()
        answer += 1
        for i in range(4):
            rp, cp = _r+dr[i], _c+dc[i]
            if 0<=rp<2**N and 0<=cp<2**N and arr[rp][cp] and (not check[rp][cp]):
                check[rp][cp] = True
                queue.append((rp, cp))
    return answer


def get_largest(arr):
    answer = 0
    check = [[False]*(2**N) for _ in range(2**N)]
    for r in range(2**N):
        for c in range(2**N):
            if not check[r][c] and arr[r][c] > 0:
                answer = max(bfs(arr, check, r, c), answer)
    return answer


for l in L:
    arr = rotate(arr, l)
    arr = melt(arr)

print(sum(map(sum, arr)))
print(get_largest(arr))
