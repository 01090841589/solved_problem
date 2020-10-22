def solution(cacheSize, cities):
    answer = 0
    LRU = [0] * cacheSize
    cache = [''] * cacheSize
    num = 0
    if cacheSize == 0:
        return len(cities) * 5
    if len(cities) == 0:
        return 0
    for id, city in enumerate(cities):
        if city.lower() not in cache:
            if num < cacheSize:
                cache[num] = city.lower()
                LRU[num] = id
                num += 1
                answer += 5
                continue
            change = LRU.index(min(LRU))
            cache[change] = city.lower()
            LRU[change] = id
            answer += 5
        else:
            change = cache.index(city.lower())
            LRU[change] = id
            answer += 1
    return answer