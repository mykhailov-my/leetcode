
"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. have a dict to store values -> index
2. iterate by string
3. if there is same key in dict -> update max_len, assighn i = (index of first occurence) + i,
assign dict with new ind
4 else add char->i to dict
5. i += 1
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        unique_chars = {}
        i = 0
        while i < len(s):
            if s[i] in unique_chars:
                max_len = max(len(unique_chars), max_len)
                i = unique_chars[s[i]] + 1
                unique_chars = {s[i]: i}
            else:
                unique_chars[s[i]] = i
            i += 1
        return max(len(unique_chars), max_len)


class Solution2:
    # Implemented with hint
    # not working break on cases 'add' and 'abcabcbb'

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        unique_chars = {}
        right = 0
        left = 0
        while right < len(s):
            if s[right] in unique_chars:
                print(f'!r({right}) - l({left}) = {right-left}; {unique_chars}')
                max_len = max(right - left, max_len)
                left = unique_chars[s[right]] + 1
                unique_chars.pop(s[right])
                unique_chars[s[left]] = left
            else:
                print(f'-r({right}) - l({left}) = {right-left}; {unique_chars}')
                unique_chars[s[right]] = right
                max_len = max(right - left, max_len)
            right += 1
        return max_len

class BestSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index != None and index >= left and index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res


class Solution4:
    '''
    Same as 1 solution but array instead of dict
    Runtime stays the same
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr_len = 0
        # unique_chars = {}
        char_map = [None] * 128
        i = 0
        while i < len(s):
            if char_map[ord(s[i])] is not None:
                max_len = max(curr_len, max_len)
                i = char_map[ord(s[i])] + 1
                char_map = [None] * 128
                char_map[ord(s[i])] = i
                curr_len = 1
            else:
                char_map[ord(s[i])] = i
                curr_len += 1
            i += 1
        return max(curr_len, max_len)


class Solution5:
    '''
    A bit optimized solution to use dict instead of list. 
    There is no significant run time change
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = right = 0
        res = 0
        while right < len(s):
            # r = s[right]

            index = char_map.get(s[right])
            if index != None and index >= left and index < right:
                left = index + 1

            res = max(res, right - left + 1)

            char_map[s[right]] = right
            right += 1
        return res


if __name__ == '__main__':
    n = "pwwkew" # 3
    n = ' '
    n = 'add'
    n = "abcabcbb"  # 3
    n = 'dvdf' # 3
    sol = Solution5()
    res = sol.lengthOfLongestSubstring(n)
    print(f'Result --> {res}')  