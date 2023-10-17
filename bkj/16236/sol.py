import sys; input=sys.stdin.readline

N = int(input())

arr =[list(map(int, input().split())) for _ in range(N)]
dist = [[0]*N for _ in range(N)]
#print(arr)

from collections import deque
def get_dist(arr, a, b, k):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    dist = [[-1]*N for _ in range(N)]
    dist[a][b] = 0
    q = deque([(a,b,0)])
    while q:
        r, c, t = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] <= k and dist[nr][nc] == -1:
                dist[nr][nc] = t+1
                q.append((nr, nc, t+1))
    return dist

K = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            r, c = i, j


INF = 99999
time = 0
eaten = 0
while True:
    dist = get_dist(arr, r, c, K)
    minDist, minLoc = INF, None
    exist=False
    for i in range(N):
        for j in range(N):
            if arr[i][j] in [1,2,3,4,5,6] and arr[i][j] < K:
                if 0 <= dist[i][j] < minDist:
                    exist = True
                    minDist = dist[i][j]
                    minLoc = (i, j)
                elif minLoc and dist[i][j] == minDist:
                    exist = True
                    if i < minLoc[0]:
                        minLoc=(i, j)
                    elif i == minLoc[0]:
                        if j < minLoc[1]:
                            minLoc = (i, j)
                        else:
                            continue
                    else:
                        continue

    #print(f"fish {K} ({eaten}/{K})", (r, c), "->", minLoc, f"distance:{minDist}, time:{time}")
    #for _n in range(N):
    #    print(dist[_n], arr[_n])

    if not exist:
        break

    # move
    arr[r][c] = 0
    arr[minLoc[0]][minLoc[1]] = 9
    time += minDist
    r, c = minLoc
    eaten += 1

    if eaten == K:
        K += 1
        eaten = 0

print(time)