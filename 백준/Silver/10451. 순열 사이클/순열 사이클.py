from collections import deque

t = int(input())

def bfs(n, permutation):
    visited = [False] * n
    count = 0

    # n번째 사이클을 찾아내기 위해서는 큐를 초기화 하고 탐색을 시작해야함
    for i in range(n): # 모든 노드 검사
        if not visited[i]: # 이미 방문한 노드는 스킵
            queue = deque()
            queue.append(i)
            visited[i] = True

            while queue:
                current = queue.popleft()
                next_node = permutation[current] -1 # 다음으로 갈 위치 (문제에서 위치는 1부터 시작하기 때문에 -1)

                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

            count += 1

    return count

for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    print(bfs(n, permutation))