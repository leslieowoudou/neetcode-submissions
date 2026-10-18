#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head:
           if head.next==None:
            return head
            
           precedent=head
           current=precedent.next
           precedent.next=None
           saver=current.next
        
           while saver is not None:
               current.next=precedent
               precedent=current
               current=saver
               saver=saver.next
           current.next=precedent
           return current
        
        
        else :
            return head

           
          
          






