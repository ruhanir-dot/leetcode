def rotateLeft(d, arr):
    stack = []
    result = []
    for i in range(d):
        stack.append(arr[i])
    
    result.extend(arr[d:])
    result.extend(stack)
    return result
         