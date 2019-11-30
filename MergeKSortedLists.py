"""
Merge k sorted linked lists and return it as one sorted list.
Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(l):
    if l:
        print l.val,
    tmp = l.next
    while tmp:
        print " -> ", tmp.val,
        tmp = tmp.next

# @param A : list of linked list
# @return the head node in the linked list
def mergeKLists(A):
    k = len(A)
    minheap = []
    cap = [0]
    
    def heapifyDown(heap, i):
        if i >= cap[0]//2:
            return
            
        left = 2*i+1
        right = 2*i+2
        smaller = i
        if heap[smaller] > heap[left]:
            smaller = left
        if right < cap[0] and heap[smaller] > heap[right]:
            smaller = right
        if i == smaller:
            return
        heap[i], heap[smaller] = heap[smaller], heap[i]
        heapifyDown(heap, smaller)
    
    def heapifyUp(heap, i):
        if i == 0:
            return 
        p = (i-2)//2
        if i & 1:
            p = (i-1)//2
        if p < 0:
            return
        if heap[p] > heap[i]:
            heap[p], heap[i] = heap[i], heap[p]
            heapifyUp(heap,p)
    
    def add(heap, v):
        if cap[0] == len(heap):
            heap.append(v)
        else:
            heap[cap[0]-1] = v
        cap[0] += 1
        heapifyUp(heap, cap[0]-1)
    
    def pop(heap):
        if cap[0] == 0:
            return
        top = heap[0]
        heap[cap[0]-1], heap[0] = heap[0], heap[cap[0]-1]
        cap[0] -= 1
        heapifyDown(heap, 0)
        return top
        
    for i in range(k):
        tmp = A[i]
        while tmp:
            add(minheap, tmp.val)
            tmp = tmp.next
    
    head = None
    if cap[0]:
        head = ListNode(pop(minheap))
    tmp = head
    while cap[0]:
        tmp.next = ListNode(pop(minheap))
        tmp = tmp.next
    return head

l1 = ListNode(1)
l1.next = ListNode(10)
l1.next.next = ListNode(20)


l2 = ListNode(4)
l2.next = ListNode(11)
l2.next.next = ListNode(13)


printList(mergeKLists([l1,l2]))
