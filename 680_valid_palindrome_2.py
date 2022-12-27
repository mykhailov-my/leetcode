"""
Status -> Implemented with solution

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        begin = 0
        end = len(s) - 1
        # is_symbol_removed = False
        removed_symbol = None
        while begin <= end:
            # print(f'{s[begin]} {s[end]}')
            if s[begin] == removed_symbol:
                begin += 1
                continue
            if s[end] == removed_symbol:
                end -= 1
                continue
            if s[begin] != s[end]:
                if s[begin + 1] == s[end] and removed_symbol is None:
                    removed_symbol = s[begin]
                    begin += 1
                elif s[begin] == s[end - 1] and removed_symbol is None:
                    removed_symbol = s[end]
                    end -= 1
                else:
                    return False
                
            begin += 1
            end -= 1
        return True

class BestSolution:
    '''
    Time complexity -> o(N)
    Space complexity -> O(1)

    Solution
    1. simple palindrome check func
    2. when first miss match has been found -> run func two times with offset
    3. if atleast one palindromevalid - > return true
    '''
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True


class Solution2:
    """
    Solved again 27 Dec
    Status -> Solved by myself

    Tags -> Two pointers, recursion

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. use two pointers
    2. during iteration if symbols unequal ->
        2.1 if we not used skip -> recursivly run this method 2 times ofsetting left and right pointers. if one of them return true -> return final true
        2.2 return false

    LC perfomance
    time -> 83%
    space -> 90% 
    """

    def validPalindrome(self, s: str, skip_allowed = True) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                if skip_allowed:
                    return self.validPalindrome(s[start+1: end+1], False) or self.validPalindrome(s[start: end], False)
                else:
                    return False
            end -= 1
            start += 1
        return True
if __name__ == '__main__':
    n = "aguokepatgbnvfqmgml cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu lmgmqfvnbgtapekouga"
    n = 'cpfxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfpc'
    n = 'cbbcc'  # True
    # n = 'abca' # True
    sol = Solution2()
    res = sol.validPalindrome(n)
    print(f'Result --> {res}')  