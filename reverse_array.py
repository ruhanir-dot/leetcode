def reverseArray(a):
    stack = []
    result = []
    for i in range(len(a)): 
        stack.append(a[i])
    for i in range(len(a)):
        result.append(stack.pop())
    
    return result
