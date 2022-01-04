import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

tmp=[]
for x in range(n):
    for y in range(n):
      if arr[x][y] != 0:
        tmp.append((arr[x][y], x, y))
tmp.sort()
q = deque(tmp)

cnt = 0
while q:
  if cnt == S:
    break
  for _ in range(len(q)):
    pre, x, y = q.popleft()
    for i in range(4):
      xx = x + dx[i]
      yy = y + dy[i]
      if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 0:
        arr[xx][yy] = arr[x][y]
        q.append((arr[xx][yy], xx, yy))
  cnt += 1

print(arr[X-1][Y-1])
