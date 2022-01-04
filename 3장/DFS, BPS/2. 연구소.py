import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ch = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0
def DFS(count):
  global res
  if count == 3:
    for x in range(n):
      for y in range(m):
        ch[x][y] = arr[x][y]
    for x in range(n):
      for y in range(m):
        if ch[x][y] == 2: virus(x, y)
    res = max(res, get_result())
    return
  for x in range(n):
    for y in range(m):
      if arr[x][y] == 0:
        arr[x][y] = 1
        DFS(count + 1)
        arr[x][y] = 0

def virus(x, y):
  for i in range(4):
    xx = x + dx[i]
    yy = y + dy[i]
    if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0:
      ch[xx][yy] = 2
      virus(xx, yy)

def get_result():
  t_res = 0
  for x in range(n):
    for y in range(m):
      if ch[x][y] == 0:
        t_res += 1
  return t_res

DFS(0)
print(res)