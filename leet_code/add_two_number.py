# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        listNode=ListNode(0,None)
        cur=listNode
        carry=0
        while(l1 is not None or l2 is not None):
            if l1 is not None:
                x=l1.val
            else:
                x=0
            if l2 is not None:
                y=l2.val
            else:
                y=0
            sum=x+y+carry
            carry=sum//10
            node=ListNode(sum%10,None)
            cur.next=node
            cur=cur.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        if carry >0:
            tail=ListNode(carry,None)
            cur.next=tail
        return listNode.next