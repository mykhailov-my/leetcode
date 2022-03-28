class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [i**2 for i in nums]
        result.sort()
        return result
        