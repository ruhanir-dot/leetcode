def printLinkedList(head):
    if head is None: 
        return None
    
    curr = head
    arr = []
    while curr is not None: 
        arr.append(curr.data)
        curr = curr.next
    for num in arr:
        print(num)
