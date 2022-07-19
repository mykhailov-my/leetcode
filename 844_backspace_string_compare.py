"""
Status -> Solved by myself

Time complexity -> O(N + M)
Space complexity -> O(N+M)

Solution
1. iterate over string
2. if its # -> pop from stack
3. else add to stack
4. compare stacks
"""
from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def str_to_stack(s):
            stack = deque()
            for char in s:
                if char == '#':
                    print(stack)
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        return str_to_stack(s) == str_to_stack(t)


class Solution2:

    def backspaceCompare(self, s: str, t: str) -> bool:
        # two pointers for each string
        pass


if __name__ == '__main__':
    n = "ab#c"
    m = "ad#c"
    n = "ab##"
    m = "c#d#"
    n = 'abc#c'
    m = 'ab#bc'

    sol = Solution()
    res = sol.backspaceCompare(n, m)
    print(f'Result --> {res}')  