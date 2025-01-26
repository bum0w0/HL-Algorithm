# 1. score 리스트 정렬 (오름차순? 내림차순?)
# 2. 인덱스 슬라이싱을 이용하여 [:m] 으로 사과 상자를 새로 구성 (근데 반복적으로 나누어 특정 크기로 분리해야함)
# 3. 새로 구성한 사과 상자를 이용해 최대 이익 계산 (최저 사과 점수 * m)


def solution(k, m, score):

    answer = 0


    sorted_score = sorted(score, reverse=True)


    for i in range(0, len(sorted_score), m):
        current_score = sorted_score[i:i+m]
        if len(current_score) == m:
            answer += min(current_score) * m

    

    return answer