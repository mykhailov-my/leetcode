# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        previous = None
        node = head
        for i in range(n + 1):
            if i == n:
                if previous is not None:
                    previous.next = node.next
                    break
            previous = node
            node = node.next
        return head


if __name__ == '__main__':
    nodes = [ListNode()]
    for i in range(1, 6):
        node = ListNode(i, next=nodes[-1])
    n = 2
    sol = Solution()
    res = sol.removeNthFromEnd(nodes[0], n)
    while res.next:
        print(res.val)
        res = res.next
    print(f'Result --> {res}')