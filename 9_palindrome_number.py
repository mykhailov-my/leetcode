"""
Status -> Solved by myself

Time complexity -> O(logN)
Space complexity -> O(logN)


"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    n = 121
    sol = Solution()
    res = sol.isPalindrome(n)
    print(f'Result --> {res}')  