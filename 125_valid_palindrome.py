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


class Solution3:
    """
    Reworked 26.12
    Status -> Solved by myself

    Tags -> Two pointers

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. iterate by string from two ends
    2. skip invalid symbols
    3. if two valid, lower symbols unequal - > return false
    4. else true

    LC 
    time - > 71%
    memory -> 50%
    """

    def is_valid_char(self, char):
        if char.isalnum():
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        while first < last:
            if not self.is_valid_char(s[first]):
                first += 1
            elif not self.is_valid_char(s[last]):
                last -= 1
            else:
                if s[first].lower() != s[last].lower():
                    return False
                first += 1
                last -= 1
        return True

if __name__ == '__main__':
    n = "A man, a plan, a canal: Panama"
    sol = Solution3()
    res = sol.isPalindrome(n)
    print(f'Result --> {res}')