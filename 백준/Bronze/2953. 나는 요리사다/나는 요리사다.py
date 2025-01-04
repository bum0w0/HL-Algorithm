answer = []

for _ in range(5):
    answer.append(sum(map(int, input().split())))
    
print(answer.index(max(answer))+1, max(answer))