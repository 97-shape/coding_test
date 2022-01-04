import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def Dummy(x, y, d):
  v = 1
  while True:
    x += dx[d]
    y += dy[d]
    if 1 <= x <= n and 1 <= y <= n and arr[x][y] != 2:
      if arr[x][y] == 0:
        a, b = snake.popleft()
        arr[a][b] = 0
      arr[x][y] = 2
      snake.append((x, y))
      if move[v] == 'L':
        d = (d-1) % 4
      elif move[v] == 'D':
        d = (d+1) % 4
      v += 1
    else:
      return v



n = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
arr[1][1] = 2
snake = deque()
snake.append((1, 1))

for _ in range(int(input())):
  x, y = map(int, input().split())
  arr[x][y] = 1

move = [0] * 10001
for _ in range(int(input())):
  x, c = input().split()
  move[int(x)] = c

print(Dummy(1, 1, 1))