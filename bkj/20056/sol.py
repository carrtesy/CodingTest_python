import sys; input=sys.stdin.readline
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]

for m in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move(arr):
    arr_new = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                for fireball in arr[r][c]:
                    m, s, d = fireball
                    rp, cp = (r + s*dr[d])%N, (c + s*dc[d])%N
                    arr_new[rp][cp].append((m, s, d))

    arr = arr_new
    for r in range(N):
        for c in range(N):
            if arr[r][c] and len(arr[r][c]) > 1:
                T = len(arr[r][c])
                new_m = sum(map(lambda x:x[0], arr[r][c])) // 5
                new_s = sum(map(lambda x:x[1], arr[r][c])) // T

                if new_m > 0:
                    if sum(map(lambda x:x[2]%2==0,arr[r][c])) == T or sum(map(lambda x:x[2]%2==1,arr[r][c])) == T:
                        arr[r][c] = [(new_m, new_s, 0), (new_m, new_s, 2), (new_m, new_s, 4), (new_m, new_s, 6)]
                    else:
                        arr[r][c] = [(new_m, new_s, 1), (new_m, new_s, 3), (new_m, new_s, 5), (new_m, new_s, 7)]
                else:
                    arr[r][c] = []
    return arr

for k in range(K):
    arr = move(arr)

total_mass=0
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            total_mass += sum(map(lambda x:x[0], arr[r][c]))
print(total_mass)
