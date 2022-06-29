"""
Status -> Solved by myself

Time complexity -> O(N+M)
Space complexity -> O(N)

Solution
1. if len is different -> return false
2. from first string create dict of characters and how many times they appear in string
3. iterate over second string, get counter from dict
4. if no character or counter zero -> return False
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        for i in s:
            s_map[i] = s_map.get(i, 0) + 1

        for j in t:
            count = s_map.get(j)
            if not count: # if no value or 0
                return False
            s_map[j] = count - 1
        return True



if __name__ == '__main__':
    n = "aacc"
    m = "ccac"
    sol = Solution()
    res = sol.isAnagram(n, m)
    print(f'Result --> {res}')  