"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        next_node = head.next
        head.next = None
        previous_node = head
        while next_node is not None:
            node = next_node
            next_node = node.next
            node.next = previous_node
            previous_node = node
        breakpoint()



if __name__ == '__main__':
    n = list_to_nodes([1,2,3,4,5])
    sol = Solution()
    res = sol.reverseList(n)
    print(f'Result --> {res}')  