"""
Status -> Solved by myself

Time complexity -> O(n)
Space complexity -> O(n)

Solution
1. create stack
2. loop through string
3. if it's open bracket '(' -> append index to stack
4. if is's close bracket ')' - pop from stack (if poped item is also ')' add two of them)
5. in case of index error -> append close bracket to stack
6. loop by stack and remove from string indexes
"""

from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                try:
                    poped_i = stack.pop()
                    if s[poped_i] == ')':
                        stack.append(poped_i)
                        stack.append(i)
                except IndexError:
                    stack.append(i)
        indexes_to_remove = set(stack)
        del stack
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)


class Solution2:
    '''
    Without stack but no win in benchmark
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        close_brackets = set()
        open_brackets = set()
        for i in range(len(s)):
            if s[i] == '(':
                open_brackets.add(i)
            elif s[i] == ')':
                if open_brackets:
                    open_brackets.pop()
                else:
                    close_brackets.add(i)
        string_builder = []
        for i in range(len(s)):
            if i in open_brackets or i in close_brackets:
                continue
            else:
                string_builder.append(s[i])
        return ''.join(string_builder)


class BestSolution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)


if __name__ == '__main__':
    n = "lee(t(c)o)de)"
    # n = '(((a)'
    n = "())()((("  # "()()"

    sol = Solution2()
    res = sol.minRemoveToMakeValid(n)
    print(f'Result --> {res}')  