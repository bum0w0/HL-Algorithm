n = int(input())
sequence = list(map(int, input().split()))
stack = []
result = [-1] * n 

for i in range(n):
    while stack and sequence[stack[-1]] < sequence[i]:
        index = stack.pop()
        result[index] = sequence[i]

    stack.append(i)

print(' '.join(map(str, result)))