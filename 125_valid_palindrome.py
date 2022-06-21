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

# Solved with hint
# Time complexity O(N)
# Space complexity O(1)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        begin = 0
        end = len(s) - 1
        while begin < end:
            while begin < end and not s[begin].isalnum():
                begin += 1
            while begin < end and not s[end].isalnum():
                end -= 1
            if s[begin].lower() != s[end].lower():
                return False
            begin += 1
            end -= 1
        return True


if __name__ == '__main__':
    n = "A man, a plan, a canal: Panama"
    sol = Solution2()
    res = sol.isPalindrome(n)
    print(f'Result --> {res}')