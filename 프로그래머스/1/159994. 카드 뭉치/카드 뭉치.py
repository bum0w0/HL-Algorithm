# 1. cards1,2 두 배열을 각각 추적할 인덱스를 사용
# 2. 검사(goal에 나온 단어와 일치하는지 검사, 순서를 만족하는지)
# 3. 단어 쓰였으면 + 1

def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0  # cards1과 cards2의 인덱스
    for word in goal:
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1  
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1  
        else:
            return "No"  # 순서대로 만들 수 없는 경우 (두개의 카드 뭉치 모두에서 찾을 수 없는 경우)
    
    return "Yes"  