"""
Status -> Implemented with solution

Time complexity -> O(N)
Space complexity -> O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f'{self.val} -> {self.next}'

def list_to_nodes(l):
    head = ListNode(l[0])
    previous_node = head
    for i in l[1:]:
        node = ListNode(i)
        previous_node.next = node
        previous_node = node
    return head


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


if __name__ == '__main__':
    n = list_to_nodes([1,2,4])
    m = list_to_nodes([1,3,4])
    sol = Solution()
    res = sol.mergeTwoLists(n, m)
    print(f'Result --> {res}')  