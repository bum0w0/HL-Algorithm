N = int(input())  # OX 퀴즈 시행 횟수

for i in range(N):
    quiz = input().strip()  # 각 퀴즈 입력
    total_points = []  # 각 퀴즈의 점수를 저장할 리스트
    count = 1  # 연속된 점수를 계산하기 위한 변수

    for char in quiz:
        if char == 'O':
            total_points.append(count)
            count += 1
        else:
            total_points.append(0)
            count = 1

    print(sum(total_points))  # 각 퀴즈의 총 점수 출력