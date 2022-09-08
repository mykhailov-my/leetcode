
class Solution:
    """
    Status -> Solved by myself
    Tags -> Two pointers

    Time complexity -> O(N)
    Space complexity -> O(N)

    Solution
    1. initiate counter of open brackets, left outter parenthese and empty list
    2. iterate by string
        3. if symbol is ( -> inrmenet openbrackets counter
        4. else -> decrement it
        5. if open bracket 1 it means we starting again, so initiate start_outter with i
        6. if open brackets == 0 means we just close all brackets -> add to result slice between start_ouuter and i,
        set start pointer to None
    7. compile string out of list and return it


    Notes 
    """
    def removeOuterParentheses(self, s: str) -> str:
        open_brackets = 0
        start_outter = None
        result = []
        for i in range(len(s)):
            if s[i] == '(':
                open_brackets += 1
            elif s[i] == ')':
                open_brackets -= 1
            if open_brackets == 1 and start_outter is None:
                start_outter = i
            if open_brackets == 0:
                result.append(s[start_outter + 1: i])
                start_outter = None
        return ''.join(result)



if __name__ == '__main__':
    n = "(()())(())(()(()))"  # "()()()()(())"
    n = '()()'
    sol = Solution()
    res = sol.removeOuterParentheses(n)
    print(f'Result --> {res}')  