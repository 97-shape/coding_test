import heapq
INF = int(1e9)

def dijikstra(start):
    q = []
    # 큐에 시작지점의 거리와 노드번호 입력
    heapq.heappush(q, (0, start))
    # 시작지점에서 시작지점 까지의 거리는 0
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        # 현재 최단 거리보다 지금의 거리가 짧은가
        if distance[now] < d:
            continue
        # 인접한 노드들 확인
        for g in graph[now]:
            # g = [(목적지 노드, 전달시간)]
            move = d + g[1]
            if move < distance[g[0]]:
                distance[g[0]] = move
                heapq.heappush(q, (move, g[0]))


n, m, c = map(int, input().split())
# 각 노드가 갈 수 있는 노드와 그 거리들을 저장하는 리스트
graph = [[] for _ in range(n+1)]
# 최단 거리 저장하는 리스트
distance = [INF] * (n+1)

# 노드 연결 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijikstra(c)

count = 0
max_distance = 0  # 총 소모 시간 = 가장 먼 거리
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count -1, max_distance)