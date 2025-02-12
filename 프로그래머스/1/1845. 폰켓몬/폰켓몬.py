def solution(nums):
    maxSelection = 0

    poketmon = set()

    for mon in nums:
        poketmon.add(mon)

    maxSelection = len(nums) // 2

    num_of_types = len(poketmon)

    return min(maxSelection, num_of_types)