"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. insert new num in sorted list using bisearch
2. if len odd return avg of two nums in middle
3. else return num from middle
"""
from bisect import bisect_left, insort


class MedianFinder:


    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        ind = bisect_left(self.nums, num)
        self.nums.insert(ind, num)

    def findMedian(self) -> float:
        if len(self.nums) % 2 != 1:
            return (self.nums[len(self.nums) // 2] + self.nums[(len(self.nums) // 2) - 1]) / 2
        return float(self.nums[len(self.nums) // 2])


class MedianFinder2:
    """
    Status -> Solved by myself

    Tags ->

    Time complexity ->
    Space complexity ->

    Solution
    1.
    2.
    3.

    Notes 
    """
    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        insort(self.values, num)

    def findMedian(self) -> float:
        mid = len(self.values) // 2
        if len(self.values) % 2 == 0:
            # breakpoint()
            return (self.values[mid] + self.values[mid - 1]) / 2
        else:
            return self.values[mid]


if __name__ == '__main__':

    finder = MedianFinder2()
    finder.addNum(1)
    finder.addNum(2)
    _ = finder.findMedian()
    print(_)
    finder.addNum(3)
    _ = finder.findMedian()
    print(_)
