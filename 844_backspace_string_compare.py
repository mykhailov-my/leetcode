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
from itertools import zip_longest

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
    '''
    Implemented from solution

    Time complexity -> O(N + M)
    Space complexity -> O(1)
    '''

    def backspaceCompare(self, s: str, t: str) -> bool:
        def symbol_iterator(s: str):
            skip = 0
            for char in reversed(s):
                if char == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield char
        return all(char_s == char_t for char_s, char_t in zip_longest(symbol_iterator(s), symbol_iterator(t)))


if __name__ == '__main__':
    n = "ab#c"
    m = "ad#c"
    n = "ab##"
    m = "c#d#"
    n = 'ddd###abc'
    m = 'abc#c'

    n = 'ab#b'
    m = 'ab'

    sol = Solution2()
    res = sol.backspaceCompare(n, m)
    print(f'Result --> {res}')  