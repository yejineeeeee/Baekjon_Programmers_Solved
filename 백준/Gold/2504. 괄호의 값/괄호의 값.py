bracket = input()
stack = []
length = len(bracket)
res = 0
tmp = 1

for i in range(length):
    b = bracket[i]
    if b == "(":
        tmp *= 2
        stack.append(b)
    elif b == "[":
        tmp *= 3
        stack.append(b)
    
    elif b == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        if bracket[i-1] == "(":
            res += tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == "(":
            res = 0
            break
        if bracket[i-1] == "[":
            res += tmp
        tmp //= 3
        stack.pop()

if stack:
    res = 0
print(res)