# 각 종의 이름을 사전순으로 출력, 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림
import sys
from collections import defaultdict

input_data = sys.stdin.read().strip().splitlines()

# 나무 이름과 개수를 저장할 dict
tree_species = defaultdict(int) # {'Ash': 1, 'Aspen': 2, 'Beech': 3} => key 는 나무이름, value 는 나무의 수
total_count = 0

# 나무 이름 개수 세기
for tree in input_data:
    tree_species[tree] += 1
    total_count += 1

# 나무 이름을 사전순으로 정렬
sorted_trees = sorted(tree_species.keys())

# 각 나무의 비율 출력
for tree in sorted_trees:
    percentage = (tree_species[tree] / total_count) * 100
    print(f"{tree} {percentage:.4f}")

# collections.defaultdict는 값(value)에 초깃값을 지정하여 딕셔너리를 생성하는 모듈이다.