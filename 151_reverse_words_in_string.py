"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. split string intow words, place them in list
2. reverse list
3. concatenate list to string
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == '__main__':
    n = "the sky is blue"
    sol = Solution()
    res = sol.reverseWords(n)
    print(f'Result --> {res}')  