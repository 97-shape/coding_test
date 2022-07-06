n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def left():
    global d
    d -= 1
    if d < 0:
        d = 3

cnt = 1  # 지금 서 있는 좌표 포함
turn = 0
while True:
    # 1
    left()
    # 2
    xx = x+dx[d]
    yy = y+dy[d]
    if 0 <= xx < n and 0 <= yy < m and not arr[xx][yy]:
        cnt += 1
        x, y = xx, yy
    else:
        turn += 1
    # 3
    if turn == 4:
        xx = x-dx[d]
        yy = y-dy[d]
        if 0 <= xx < n and 0 <= yy < m and not arr[xx][yy]:
            x, y = xx, yy
            turn = 0
        else:
            print(cnt)
            break
