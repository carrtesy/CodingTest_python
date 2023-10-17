import sys; input=sys.stdin.readline

N, M = map(int, input().split())
A, B, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

cnt = 0
while True:
    if arr[A][B] == 0:
        arr[A][B] = -1
        cnt += 1

    found = False
    for i in range(4):
        d = (d-1)%4
        nA, nB = A+dr[d], B+dc[d]
        if 0<=nA<N and 0<=nB<M and arr[nA][nB] == 0:
            found=True
            A, B = nA, nB
            break

    if not found:
        nA, nB = A-dr[d], B-dc[d]
        if arr[nA][nB] == 1:
            break
        else:
            A, B = nA, nB
print(cnt)