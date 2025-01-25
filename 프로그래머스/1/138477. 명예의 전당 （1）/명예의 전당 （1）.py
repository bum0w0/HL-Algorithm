def solution(k, score):
    answer = []
    hof_scores = []

    for i in score:
        hof_scores.append(i)

        # 내림차순
        hof_scores.sort(reverse=True)

        # k개의 점수만 유지
        if len(hof_scores) > k:
            hof_scores = hof_scores[:k]

        answer.append(hof_scores[-1])  # 리스트의 마지막 요소가 최솟값 (내림차순 했으니깐)

    return answer