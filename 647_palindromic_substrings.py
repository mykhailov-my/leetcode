"""
Status -> Solved with hint

Time complexity -> O(n^3)
Space complexity -> O(N)

inefficient

Solution
1. nested list in rage of string len
2. check if substring palindrome
3. if string is palindrome cache it
"""

class Solution:
    palindromes = set()
    
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub_string = s[i:j]
                if self.is_palindrome(sub_string):
                    counter += 1
        return counter

    def is_palindrome(self, s: str) -> bool:
        if s in self.palindromes:
            return True
        begin = 0
        end = len(s) - 1
        while begin <= end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        self.palindromes.add(s)
        return True


class BestSolution:
# Time complexity -> O(n^2)
# Space complexity -> O(1)

    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            counter += self.count_around_center(s, i, i)
            counter += self.count_around_center(s, i, i + 1)
        return counter

    def count_around_center(self, s, left, right):
        counter = 0
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            else:
                counter += 1
                left -= 1
                right += 1
        return counter


if __name__ == '__main__':
    n = "ababa"
    sol = BestSolution()
    res = sol.countSubstrings(n)
    print(f'Result --> {res}')  