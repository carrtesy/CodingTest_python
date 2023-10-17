import sys; input=sys.stdin.readline
import copy

arr = []
head = []
for i in range(4):
    lst = list(map(int, input().split()))
    arr.append([lst[j] for j in range(0, 8, 2)])
    head.append([lst[j]-1 for j in range(1, 8, 2)])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def play(arr, head):
    for k in range(1, 16+1):
        moved = False
        for i in range(4):
            for j in range(4):
                if arr[i][j] == k:
                    # print(f"K: {k}")

                    for p in range(8):
                        ni, nj = i+dr[head[i][j]], j+dc[head[i][j]]
                        if 0<=ni<4 and 0<=nj<4 and arr[ni][nj]!=-1:

                            if arr[ni][nj] > 0:
                                tmp = arr[i][j]
                                arr[i][j] = arr[ni][nj]
                                arr[ni][nj] = tmp
                                tmp = head[i][j]
                                head[i][j] = head[ni][nj]
                                head[ni][nj] = tmp
                            else:
                                arr[ni][nj] = arr[i][j]
                                head[ni][nj] = head[i][j]
                                arr[i][j] = 0

                            # for _p in range(4):
                            #     print(arr[_p])
                            # for _p in range(4):
                            #     print(head[_p])
                            moved=True
                            break
                        else:
                            head[i][j] = (head[i][j] + 1) % 8
                if moved: break
            if moved: break
        if moved:
            continue

answer = 0

def dfs(arr, head, r, c, shark_head, fishes):
    global answer
    answer = max(answer, sum(fishes))

    play(arr, head)
    arr_temp = copy.deepcopy(arr)
    head_temp = copy.deepcopy(head)

    max_fish = 0
    for i in range(1, 5):
        nr, nc = r+i*dr[shark_head], c+i*dc[shark_head]
        if 0<=nr<4 and 0<=nc<4 and arr[nr][nc] > 0:
            fishes.append(arr[nr][nc])
            arr[r][c] = 0
            arr[nr][nc] = -1
            dfs(arr, head, nr, nc, head[nr][nc], fishes)
            fishes.pop()
        arr = copy.deepcopy(arr_temp)
        head = copy.deepcopy(head_temp)

    return max_fish

fishes=[arr[0][0]]
arr[0][0] = -1
dfs(arr, head, 0, 0, head[0][0], fishes)
print(answer)