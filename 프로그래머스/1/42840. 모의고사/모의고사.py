from collections import defaultdict
def solution(answers):
    answer = []

    # 수포자들 패턴
    math_dropout1 = [1, 2, 3, 4, 5]
    math_dropout2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_dropout3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = defaultdict(int)  # 각 수포자와 점수를 저장

    for i in range(len(answers)):  
        if answers[i] == math_dropout1[i % len(math_dropout1)]:  
            scores[1] += 1  
        if answers[i] == math_dropout2[i % len(math_dropout2)]:  
            scores[2] += 1  
        if answers[i] == math_dropout3[i % len(math_dropout3)]:  
            scores[3] += 1  
    
    max_score = max(scores.values()) # 가장 높은 점수를 받은 수포자(들)

    for i in range(1, 4): 
        if scores[i] == max_score:
            answer.append(i)

    return answer