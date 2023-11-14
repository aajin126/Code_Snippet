INF = int(1e9)

n = int(input())# 노드 개수
m = int(input())# 간선 개수

graph = [[INF]*(n + 1) for _ in range(n + 1)] # 노드 정보를 담는 리스트

#자기 자신으로 가는 노드는 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선간의 정보로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] != INF:
        if graph[a][b] > c :
            graph[a][b] = c
    else:
        graph[a][b] = c
    

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("0", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()