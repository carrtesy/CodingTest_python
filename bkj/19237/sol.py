import sys; input=sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N)]
d = list(map(lambda x:int(x)-1, input().split()))
for r in range(N):
    for c in range(N):
        if arr[r][c] == -1:
            arr[r][c] = None
        else:
            shark = arr[r][c]
            arr[r][c] = (shark, d[shark])

scent = [[None]*N for _ in range(N)]
pref = []

for m in range(M):
    pref.append([list(map(lambda x:int(x)-1, input().split())) for _ in range(4)])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def poop(arr, scent):
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                shark, _ = arr[r][c]
                scent[r][c] = (shark, K)

def diminish(scent):
    for r in range(N):
        for c in range(N):
            if scent[r][c]:
                shark, d = scent[r][c]
                if d <= 1:
                    scent[r][c] = None
                else:
                    scent[r][c] = (shark, d-1)

def move(arr, scent):
    to_move = []
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                shark, d = arr[r][c]
                to_move.append((shark, d, r, c))


    for (shark, d, r, c) in to_move:
        move_success = False
        for case in range(4):
            pref_d = pref[shark][d][case]
            rp, cp = r+dr[pref_d], c+dc[pref_d]
            if 0<=rp<N and 0<=cp<N:
                if scent[rp][cp] is None:
                    if arr[rp][cp]:
                        new_shark, _ = arr[rp][cp]
                        if shark < new_shark:
                            arr[rp][cp] = (arr[r][c][0], pref_d)
                    else:
                        arr[rp][cp] = (arr[r][c][0], pref_d)
                    arr[r][c] = None
                    move_success=True
                    break

        if move_success:
            continue
        else:
            for case in range(4):
                pref_d = pref[shark][d][case]
                rp, cp = r + dr[pref_d], c + dc[pref_d]
                if 0 <= rp < N and 0 <= cp < N:
                    if scent[rp][cp]:
                        sc_shark, _ = scent[rp][cp]
                        if sc_shark == shark:
                            if arr[rp][ cp]:
                                new_shark, _ = arr[rp][cp]
                                if shark < new_shark:
                                    arr[rp][cp] = (arr[r][c][0], pref_d)
                            else:
                                arr[rp][cp] = (arr[r][c][0], pref_d)
                            arr[r][c] = None
                            break

def one_survived(arr):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                cnt += 1
    return cnt<=1

sec = 0
poop(arr, scent)

while sec <= 1000:
    sec += 1
    move(arr, scent)
    diminish(scent)
    poop(arr, scent)
    if one_survived(arr):
        break

if sec > 1000:
    print(-1)
else:
    print(sec)