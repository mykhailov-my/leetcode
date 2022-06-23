"""
Status -> Solved by myself

Time complexity -> O(N + M + log(SUM))
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

if __name__ == '__main__':
    first = build_list(342)
    second = build_list(465)
    sol = Solution()
    res = sol.addTwoNumbers(first, second)
    print(f'Result --> {res}')  