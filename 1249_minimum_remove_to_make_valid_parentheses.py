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

        while len(stack) > 0:
            index_to_remove = stack.pop()
            s = s[:index_to_remove] + s[index_to_remove+1:]
        print(stack)
        return s



if __name__ == '__main__':
    n = "lee(t(c)o)de)"
    sol = Solution()
    res = sol.minRemoveToMakeValid(n)
    print(f'Result --> {res}')  