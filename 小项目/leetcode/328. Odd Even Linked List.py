class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
def oddEvenList(head):
    temp = head
    sec = head.next
    while temp.next.next != None:
        a = temp.next
        temp.next = temp.next.next
        temp = temp.next
        if temp.next != None:
            a.next = temp.next
        else:
            a.next = None
            temp.next = sec
    a = temp.next
    a.next = None
    temp.next = sec
    return head
'''
    
def oddEvenList(head):
    if not head:
        return head

    oddPointer = head
    evenPointer = head.next
    temp = head.next #this is the part where I changed
    while evenPointer and evenPointer.next:
        oddPointer.next = evenPointer.next
        oddPointer = oddPointer.next
        evenPointer.next = oddPointer.next
        evenPointer = evenPointer.next

    oddPointer.next = temp #this is the part where I changed
    return head

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    def main(a):
        print(a.val)
        while a.next != None:
            print(a.next.val)
            a = a.next
    oddEvenList(a)
    main(a)
    
