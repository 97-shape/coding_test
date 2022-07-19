n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  # 지도 이탈시
        return False
    # 미방문 지역일 시
    if arr[x][y] == 0:
            arr[x][y] = 1
            # 시계방향 수색
            DFS(x-1, y)
            DFS(x, y+1)
            DFS(x+1, y)
            DFS(x, y-1)
            return True
    # 지도에는 속하지만 방문한 지역일 때
    return False

res = 0
for x in range(n):
    for y in range(m):
        if DFS(x, y) == True:
            res += 1
print(res)