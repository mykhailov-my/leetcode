from random import randint


class Solution:
    """
    Status -> Solved with hint

    Tags -> Quick select

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1.
    2.
    3.

    Notes 
    """
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition(left, right, pivot_ind):
            pivot = nums[pivot_ind]
            nums[pivot_ind], nums[right] = nums[right], nums[pivot_ind]
            store = left
            for i in range(left, right + 1):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[right], nums[store] = nums[store], nums[right]
            return store
        
        def select(left, right, k):
            if left == right:
                return nums[left]
            rnd = randint(left, right)
            pivot_ind = partition(left, right, rnd)
            # breakpoint()
            if k == pivot_ind:
                return nums[k]
            elif k < pivot_ind:
                return select(left, pivot_ind-1, k)
            else:
                return select(pivot_ind + 1, right, k)
        ind = select(0, len(nums) -1, len(nums) -k)
        print(ind)
        return ind



if __name__ == '__main__':
    n = [3,2,1,5,6,4]  # 5
    k = 2
    n = [3,2,3,1,2,4,5,5,6]  # 4
    k = 4
    sol = Solution()
    res = sol.findKthLargest(n, k)
    print(f'Result --> {res}')  