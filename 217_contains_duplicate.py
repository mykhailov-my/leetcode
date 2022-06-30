"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity -> O(n)
Space complexity -> O(n)

Solution
1. convert list to set
2. check if len of lst and set is equal 
3.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)



if __name__ == '__main__':
    n = [1,1,1,3,3,4,3,2,4,2]
    sol = Solution()
    res = sol.containsDuplicate(n)
    print(f'Result --> {res}')  