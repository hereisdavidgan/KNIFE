#########################################################
"""242. 有效的字母异位词"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s)==Counter(t):
            return True
        else:
            return False


#########################################################
"""141. 环形链表"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        car, bike = head, head
        while car and car.next:
            bike = bike.next
            car = car.next.next
            if car == bike:
                return True
        return False 
#########################################################