"""
Status -> Implemented with solution

"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        sum_ = 0
        value_counter = {0: 1}
        for num in nums:
            sum_ += num
            count += value_counter.get(sum_ - k, 0)
            value_counter[sum_] = value_counter.get(sum, 0) + 1
        return count

class BestSolution:
    '''
    Time complexity -> O(N)
    Space complexity -> O(N)

    Solution
    1. assign dict value counter {0:1}, result and prefixsum vars
    2. iterate over nums
    3. increment prefixsub by num
    4. if value counter have key (prefix sum - k) -> add counter value to result
    5. add prefixsum to value counter (increment if exist, else 1)
    '''
    def subarraySum(self, nums: list[int], k: int) -> int:

        result = 0
        prefsum = 0
        value_counter = {0:1}

        for num in nums:
            prefsum += num
            print(prefsum)
            if prefsum-k in value_counter:
                result += value_counter[prefsum-k]
            value_counter[prefsum] = value_counter.get(prefsum, 0) + 1
        print(value_counter)
        return result



if __name__ == '__main__':
    n = [1,2,3,2,-1,-2,4]
    n = [2, 1, 1, 1, -1]
    k = 3
    sol = BestSolution()
    res = sol.subarraySum(n, k)
    print(f'Result --> {res}')  