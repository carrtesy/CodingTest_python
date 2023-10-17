import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
dr = [0, 0,-1,-1,-1,0,1,1,1]
dc = [0,-1,-1, 0,1,1,1,0, -1]
er = [-1, 1, 1,-1]
ec = [ 1, 1,-1,-1]

for _ in range(M):
  #1
  d, s = map(int, input().split())
  new_cloud = []
  for (r, c) in cloud:
    rp, cp = (r+s*dr[d]+N)%N,(c+s*dc[d]+N)%N 
    new_cloud.append((rp, cp))
  
  #2
  for (r, c) in new_cloud:
    A[r][c] += 1

  #3,4 
  update = []
  for (r, c) in new_cloud:
    cnt = 0
    for i in range(4):
      rp, cp = r+er[i], c+ec[i]
      if 0<=rp<N and 0<=cp<N and A[rp][cp]:
        cnt+=1
    update.append((r, c, cnt))
  for (r, c, cnt) in update:
    A[r][c] += cnt
    
  #5
  cloud = []
  for r in range(N):
    for c in range(N):
      if A[r][c] >=2 and (r, c) not in new_cloud:
        cloud.append((r, c))
        A[r][c] -= 2

print(sum(map(sum, A)))