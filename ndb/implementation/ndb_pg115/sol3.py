loc = input()
print(loc)

r, c = ord(loc[0]) - ord('a') , int(loc[1])

print(r, c)

dr = [1, 1, -1, -1, 2, -2, 2, -2]
dc = [2, -2, 2, -2, 1, 1, -1, -1]

cnt = 0
for i in range(8):
    nr, nc = r+dr[i], c+dc[i]
    if 1<=nr<=8 and 1<=nc<=8: cnt+=1
print(cnt)