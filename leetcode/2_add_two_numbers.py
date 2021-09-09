class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(7, ListNode(0, ListNode(8)))


# immutable objects such as int, float and str: a = b = 1, b += 1, b = 2, a = 1
# mutable objects such as dict, list and objects: a = b = [1, 2], b[0] = 2, b = [2, 2], a = [2, 2]
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = recur = ListNode(0)
        num = 0
        while l1 or l2 or num:
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            recur.next = ListNode(num%10)
            recur = recur.next
            num = num//10
        return output.next
