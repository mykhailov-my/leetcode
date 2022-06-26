"""
Status -> Solved by myself

Time complexity -> O(N + M)
Space complexity -> O(log N)

Solution
1. nums to list onvertor
    convert number to list of digits 
    create nodes from each digit
2. List to num convertor
    loop through nodes
    on each iteration add number to counter multipled by 10 powered to iteration step
3. convert lists to nums, add, convert back to list
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f'ListNode(v={self.val}, next={self.next})'


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return build_list(from_list_to_num(l1) + from_list_to_num(l2))

def from_list_to_num(node):
    counter = 0
    multiplier = 1
    while node is not None:
        counter += node.val * multiplier
        multiplier *= 10
        node = node.next

    return counter

def build_list(num):
    num_list = [int(i) for i in str(num)]
    previous_node = None
    for i in num_list:
        node = ListNode(i, previous_node)
        previous_node = node

    return previous_node


class Solution2:
    # Time complexity O(N + M)
    # Space complexity O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        l1_node = l1
        l2_node = l2
        while l1_node or extra:
            l1_val = l1_node.val if l1_node else 0
            l2_val = l2_node.val if l2_node else 0
            if l1_node:
                l1_node.val = (l1_val + l2_val + extra) % 10
            else:
                l1_node = ListNode((l1_val + l2_val + extra) % 10)
                last_node.next = l1_node
            extra = (l1_val + l2_val + extra) // 10

            if l2_node and l1_node.next is None and l2_node.next is not None:
                l1_node.next = l2_node.next
                l2_node.next = None

            if l1_node.next is None:
                last_node = l1_node
            l1_node = l1_node.next if l1_node else None
            l2_node = l2_node.next if l2_node else None
        return l1


if __name__ == '__main__':
    first = build_list(0)
    second = build_list(37)
    sol = Solution2()
    res = sol.addTwoNumbers(first, second)
    res2 = from_list_to_num(res)
    print(f'Result --> {res2}')
    print(f'Result --> {res}')