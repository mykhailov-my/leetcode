"""
Status -> Solved by myself

Time complexity -> O(N^2)
Space complexity -> O(N^2)

Solution
1. pre-build key -> symbols mapper
2. merge two lists
    3. iterate by first list, nested iterate by second list
    4. append to result str concatenation
5 iterate by digits and merge result with num from mapper
"""

class Solution:
    num_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    def letterCombinations(self, digits: str) -> list[str]:
        def combine_lists(l1, l2):
            if len(l1) == 0: return l2
            res = []
            for s1 in l1:
                for s2 in l2:
                    res.append(s1+s2)
            return res
        res = []
        for digit in digits:
            res = combine_lists(res, self.num_map[digit])
        return res



if __name__ == '__main__':
    n = "23"  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    sol = Solution()
    res = sol.letterCombinations(n)
    print(f'Result --> {res}')  