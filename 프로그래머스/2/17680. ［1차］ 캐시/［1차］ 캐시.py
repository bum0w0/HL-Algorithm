def solution(cacheSize, cities):

    cache = []
    time = 0
    # 문제 조건에서 대소문자 구분을 하지 않는다고 함.
    # "NewYork"이 저장되어 있어도 "newyork"을 찾으려고 하면 캐시미스가 될 수 있기 때문에 도시 이름을 모두 소문자로 처리
    cities = [city.lower() for city in cities]

    for city in cities:
        if cacheSize == 0:
            time += 5
            continue

        if city in cache:
            cache.pop(cache.index(city))
            cache.append(city)
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            time += 5    
        
    return time