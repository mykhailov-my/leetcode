
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        hashed_nums = set(nums)
        for i in range(len(nums), -1, -1):
            if i not in hashed_nums:
                return i
        

if __name__ == '__main__':
    n = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    res = sol.missingNumber(n)
    print(f'Result --> {res}')