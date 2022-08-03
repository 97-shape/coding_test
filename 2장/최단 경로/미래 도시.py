INF = int(1e9)  # int형 최대값

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        # 자기 자신으로 가는 경우일 때
        if i == j:
            graph[i][j] = 0

# graph 입력받아 채우기
for _ in range(m):
    x, y = map(int, input().split())
    # 모든 이동시간은 1만큼 소모된다.
    graph[x][y] = 1
    graph[y][x] = 1

# 목적지와 거처야되는 장소 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 실시
for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][c]+graph[c][b])

result = graph[1][k] + graph[k][m]

if result < INF:
    print(result)
else:
    print(-1)