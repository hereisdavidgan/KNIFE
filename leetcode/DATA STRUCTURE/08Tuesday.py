l1 = [1,2,4]
l2 = [1,3,4]

for i in l2:
    l1.append(i)
l1.sort()
print(l1)
#########################################################
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
#########################################################
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            next_node = head.next 
        else:
            next_node = head
        return next_node