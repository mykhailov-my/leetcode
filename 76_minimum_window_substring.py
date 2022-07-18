"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''
        desired_val_counter = {}
        for char in t:
            desired_val_counter[char] = desired_val_counter.get(char, 0) + 1
        
        desired_val_indices = {}
        for i, char in enumerate(s):
            if char in desired_val_counter:
                desired_val_indices[char] = desired_val_indices.get(char, []) + [i]
        print(desired_val_counter)
        print(desired_val_indices)



if __name__ == '__main__':
    s = "ADOBBECODEBBANCABB"
    t = "ABCB"
    sol = Solution()
    res = sol.minWindow(s,t)
    print(f'Result --> {res}')  