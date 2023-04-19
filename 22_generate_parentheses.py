
class Solution:
    """
    Status -> Solved by myself

    Tags -> Backtracking, DP

    Time complexity -> O(N!)
    Space complexity -> O(N)

    Solution
    1. recursivly build a prefix keeping track how many open and closed brackets is being used
    2. We can build open brackets to the limit N, so if we can add it -> call func with added ( in prefix 
    3. Closed parentheses can't exceed limit N and amount of open parentheses
    4. if we reached limit for open and closed parentheses -> build for single option done, return prefix

    Notes 
    """
    def build_string(self, prefix, used_open, used_close, limit):
        if used_open >= limit and used_close >= limit:
            return [prefix]
        result = []
        if used_open < limit:
            sub_result = self.build_string(prefix + '(', used_open+1, used_close, limit)
            result.extend(sub_result)
        if used_close < limit and used_close < used_open:
            sub_result = self.build_string(prefix + ')', used_open, used_close+1, limit)
            result.extend(sub_result)
        return result

    def generateParenthesis(self, n: int) -> list[str]:
        return self.build_string('', 0, 0, n)


if __name__ == '__main__':
    # (())(())
    n = 3  # ["((()))","(()())","(())()","()(())","()()()"]
    # n = 2  # ["(())", "()()"]
    n = 4  # ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    sol = Solution()
    res = sol.generateParenthesis(n)
    print(f'Result --> {res}')
