# Solved by myself
# Time complexity O(log N)
# Space complexity O(log N)

# Solution
# use modified binary search
# select mid, if left and right lesser then mid -> mid is a result
# find what neighbour is bigger to select side
# repeat search by selected side
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        return self.bin_search(arr, 0, len(arr) - 1)

    def bin_search(self, arr, begin, end):
        mid = int((end + begin)/ 2)
        left_num = arr[mid-1] if mid > 0 else 0
        right_num = arr[mid+1] if mid <  len(arr) - 1 else 0
        if arr[mid] > left_num and arr[mid] > right_num:
            return mid
        if left_num > arr[mid]:
            return self.bin_search(arr, begin, mid)
        elif right_num > arr[mid]:
            return self.bin_search(arr, mid, end)


if __name__ == '__main__':
    n = [18,29,38,59,98,100,99,98,90]
    sol = Solution()
    res = sol.peakIndexInMountainArray(n)
    print(f'Result --> {res}')  