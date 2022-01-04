n = int(input())
plans = list(input().split())

x, y = 1, 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
move = ['U', 'R', 'D', 'L']

for m in plans:
  for i in range(4):
    if m == move[i]:
      xx = x + dx[i]
      yy = y + dy[i]
      if 1 <= xx <= n and 1 <= yy <= n:
        x, y = xx, yy

print(xx, yy)
