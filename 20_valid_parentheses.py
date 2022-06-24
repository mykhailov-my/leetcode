"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""
from collections import deque

class Solution:
    parenthes_mapper = {
        "{": "}",
        "(": ")",
        "[": "]",
    }

    def isValid(self, s: str) -> bool:
        stack = deque()
        for parenthes in s:
            if parenthes in {"{", "(", "["}:
                stack.append(parenthes)
            else:
                try:
                    previous_parenthes = stack.pop()
                except IndexError:
                    return False
                if self.parenthes_mapper[previous_parenthes] != parenthes:
                    return False
        return len(stack) == 0



if __name__ == '__main__':
    n = "()[]{}{)"
    sol = Solution()
    res = sol.isValid(n)
    print(f'Result --> {res}')  