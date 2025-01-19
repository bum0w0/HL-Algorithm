# deque를 사용한 풀이
from collections import deque

def solution(cacheSize, cities):
    
    cache = deque(maxlen=cacheSize)  # deque에 maxlen 설정
    time = 0

    for city in cities:
        city = city.lower()  # 대소문자 구분이 없으므로 소문자로 변환
        
        if city in cache:
            # 캐시 히트: 기존 위치 제거 후 다시 삽입
            # 기존에 항목을 인덱스로 찾은 후 pop으로 제거하지 않고 직접 값을 찾아 제거할 수 있는 remove 메소드 사용 (deque 특징)
            cache.remove(city)
            cache.append(city) # 가장 최근 사용으로 갱신
            time += 1
        else:
            # 캐시 미스: 캐시가 꽉 차면 가장 오래된 항목 자동 제거 후 삽입
            cache.append(city) # deque의 maxlen 덕분에 크기가 초과되면 가장 오래된 항목이 자동으로 제거
            time += 5

    return time