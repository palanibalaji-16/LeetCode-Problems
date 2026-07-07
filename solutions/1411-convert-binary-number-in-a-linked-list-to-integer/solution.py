# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        l=[]
        c=head
        while c:
            l.append(str(c.val))
            c=c.next
        b="".join(l)
        return int(b,2)
        
