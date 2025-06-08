n = int(input())
personA, personB = map(int, input().split()) # 시작노드 7, 도착노드 3
m = int(input())
graph = [[] for _ in range(n+1)] # 사람들을 나타내는 번호가 1부터 시작
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1 # 친척 관계가 없으면 -1

def dfs(node, cnt):
    global count
    visited[node] = True

    if node == personB:
        count = cnt
        return

    for distance in graph[node]:
        if not visited[distance]:
            dfs(distance, cnt+1) # 다음 노드로 이동할 때 촌수(cnt)를 1 증가

dfs(personA, 0)
print(count)