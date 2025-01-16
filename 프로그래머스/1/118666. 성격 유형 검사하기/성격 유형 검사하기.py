def solution(survey, choices):
    score_map = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    types = ["R", "T", "C", "F", "J", "M", "A", "N"]
    scores = {}

    for t in types:
        scores[t] = 0
    
    for i in range(len(survey)):
        choice = choices[i]
        first, second = survey[i][0], survey[i][1]
        
        if choice < 4:  # 첫 번째 유형
            scores[first] += score_map[choice]
        elif choice > 4:  # 두 번째 유형
            scores[second] += score_map[choice]

    result = ""
    indicator = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    for first, second in indicator:
        if scores[first] >= scores[second]:
            result += first
        else:
            result += second
    
    return result