# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val} -> {self.next}'

    def __repr__(self) -> str:
        return self.__str__()


def create_input(inp: list[int]):
    head = ListNode(inp[0])
    previous = head
    for j in inp[1:]:
        node = ListNode(j)
        previous.next = node
        previous = node
    return head



class Solution:
    """
    Status -> Solved with hint

    Tags -> Two pointers, Linked list

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. create fake node and add in front
    2. create first pointer, itarete it Nth times in list, starting from fake node
    3. create second pointer
    4. iterate first and second simultaniously untill the end
    5. At this point second pointer right before node that we have to remove, so remove it
    6. return fake node next, cos head can be removed as well

    Notes 
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake_node = ListNode(0, head)
        first = fake_node
        for i in range(n + 1):
            first = first.next

        second = fake_node
        while first is not None:
            first = first.next
            second = second.next
        if second.next is None or second.next.next is None:
            second.next = None
        else:
            second.next = second.next.next
        return fake_node.next
            


if __name__ == '__main__':
    head = create_input([1,2,3,4,5])
    i = 2
    # head = create_input([1,2])
    # i = 2
    sol = Solution()
    res = sol.removeNthFromEnd(head, i)
    print(f'Result --> {res}')