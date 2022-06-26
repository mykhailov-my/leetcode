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


class Solution2:
    # Solution basicaly the same but without recursion
    # Time complexity O(log N)
    # Space complexity O(1)
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        begin = 0
        end = len(arr) - 1

        while True:
            mid = (end + begin) // 2
            left_num = arr[mid-1] if mid > 0 else 0
            right_num = arr[mid+1] if mid <  len(arr) - 1 else 0
            if arr[mid] > left_num and arr[mid] > right_num:
                return mid
            if left_num > arr[mid]:
                end = mid
                continue
            elif right_num > arr[mid]:
                begin = mid
                continue


class Solution3:
    # Solution based on leet code solution, simpler
    # Time complexity O(log N)
    # Space complexity O(1)
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        begin = 0
        end = len(arr) - 1
        while begin < end:
            mid = (end + begin) // 2
            if arr[mid + 1] > arr[mid]:
                begin = mid + 1
            else:
                end = mid
        return begin


if __name__ == '__main__':
    n = [18,29,38,59,98,100,99,98,90]
    sol = Solution3()
    res = sol.peakIndexInMountainArray(n)
    print(f'Result --> {res}')  