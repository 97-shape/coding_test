from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()  
q.append((0, 0))# (1, 1)좌표부터 탐색 시작
while q:
    x, y = q.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 1:
            arr[xx][yy] = arr[x][y] + 1
            q.append((xx, yy))

print(arr[n-1][m-1])