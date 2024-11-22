n = int(input())
sequence = [int(input()) for _ in range(n)]  # 수열
stack = []  # 스택
result = []  # 연산 (+, -)

current = 1 
for num in sequence:
    # num이 스택의 top과 일치할 때까지 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    # 스택의 top이 num과 같으면 pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    print('\n'.join(result))