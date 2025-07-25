from collections import deque

a, p = map(int, input().split())

def get_next_number(x, p):
    return sum(int(d)**p for d in str(x))

def bfs(a, p):
    queue = deque()
    visited = dict() # key: 수, value: 해당 수가 처음 등장한 인덱스

    queue.append(a) # 탐색을 시작할 숫자 추가 (가장 처음 숫자)
    visited[a] = 0 # 처음 숫자 방문 처리
    index = 1 # 인덱스는 1로 갱신

    while queue:
        current = queue.popleft()
        next_num = get_next_number(current, p)

        if next_num in visited: # 반복이 시작되는지 검사
            return visited[next_num] # 처음 반복 시작된 수의 인덱스 반환 ( = 반복이 시작되기 전에 나온 수의 개수)
        
        # 새로운 숫자일 때 해야 할 일들
        visited[next_num] = index # 몇 번째인지 기록
        queue.append(next_num) # 큐에 넣어서 수열을 확장
        index += 1 # 인덱스 갱신

print(bfs(a, p))