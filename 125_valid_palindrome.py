# Solved by myself
# Time complexity O(n)
# Space complexity O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalpha() or i.isnumeric()])
        begin = 0
        end = len(s) - 1
        while begin <= end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True

if __name__ == '__main__':
    n = "0P"
    sol = Solution()
    res = sol.isPalindrome(n)
    print(f'Result --> {res}')