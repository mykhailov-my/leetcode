"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(n)

Solution
1. Create stack
2. If it's opening parenthesis add it to stack
3. else pop last item from stack, if stack empty or parenthesis missmatch return false
4. return if stack is empty
"""
from collections import deque

class Solution:
    parenthesis_mapper = {
        "{": "}",
        "(": ")",
        "[": "]",
    }

    def isValid(self, s: str) -> bool:
        stack = deque()
        for parenthesis in s:
            if parenthesis in {"{", "(", "["}:
                stack.append(parenthesis)
            else:
                try:
                    previous_parenthes = stack.pop()
                except IndexError:
                    return False
                if self.parenthesis_mapper[previous_parenthes] != parenthesis:
                    return False
        return len(stack) == 0



if __name__ == '__main__':
    n = "()[]{}{)"
    sol = Solution()
    res = sol.isValid(n)
    print(f'Result --> {res}')  