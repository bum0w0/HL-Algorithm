# 입력 받기
N = int(input())                     # 리스트의 크기 N
numbers = list(map(int, input().split()))  # N개의 정수 리스트
v = int(input())                     # 찾을 숫자 v

# 개수 세기
count = numbers.count(v)

# 결과 출력
print(count)