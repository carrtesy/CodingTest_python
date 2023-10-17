import sys; input=sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

r, c = N//2, N//2
OUT = 0

dr = [0,1,0,-1]
dc = [-1,0,1,0]

def add_tuple(a, x, b=None, y=None):
    if b and y:
        return (a*x[0]+b*y[0], a*x[1]+b*y[1])
    else:
        return (a*x[0], a*x[1])

def wind(arr, cur, d):
    global OUT
    r, c = cur
    if arr[r+dr[d]][c+dc[d]]:
        sand = arr[r+dr[d]][c+dc[d]]
        forward = (dr[d], dc[d])
        left = (dr[(d+1)%4], dc[(d+1)%4])
        right = (dr[(d+3)%4], dc[(d+3)%4])
        offsets = [
            (add_tuple(3, forward), int(sand*0.05)),
            (add_tuple(1, left), int(sand * 0.01)),
            (add_tuple(1, right), int(sand * 0.01)),
            (add_tuple(1, forward, 1, left), int(sand * 0.07)),
            (add_tuple(1, forward, 1, right), int(sand * 0.07)),
            (add_tuple(2, forward, 1, left), int(sand * 0.10)),
            (add_tuple(2, forward, 1, right), int(sand * 0.10)),
            (add_tuple(1, forward, 2, left), int(sand * 0.02)),
            (add_tuple(1, forward, 2, right), int(sand * 0.02)),
        ]
        except_alpha = sum(map(lambda x:x[1], offsets))
        offsets.append((add_tuple(2, forward), sand - except_alpha))


        arr[r+dr[d]][c+dc[d]] = 0
        for (offset, amount) in offsets:
            rp, cp = add_tuple(1, (r, c), 1, offset)
            if 0<=rp<N and 0<=cp<N:
                arr[rp][cp] += amount
            else:
                OUT += amount

d = 0
for s in range(1, N):
    for _ in range(s):
        wind(arr, (r, c), d)
        r, c = r+dr[d], c+dc[d]
    d = (d+1)%4
    for _ in range(s):
        wind(arr, (r, c), d)
        r, c = r+dr[d], c+dc[d]
    d = (d+1)%4

for _ in range(N-1):
    wind(arr, (r, c), d)
    r, c = r+dr[d], c+dc[d]

print(OUT)