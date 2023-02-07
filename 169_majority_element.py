from collections import Counter


class Solution:
    """
    Status -> Solved by myself

    Time complexity -> O(n), (79.7% score)
    Space complexity -> O(n), (80.9% score)

    """
    def majorityElement(self, nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


class Solution2:
    """
    Status -> Implemented with solution


    Time complexity -> O(n) (score 86%)
    Space complexity -> O(1) (score 81%)

    Solution
    (it's a Moore's Voting Algorithm)
    1. set candidate and votes counter (null and 0)
    2. iterate by array
        3. if votes 0 -> assign new candidate as current
        4. if current num == to candidate we increment votes, otherwise decrement

    """
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        votes = 0
        for num in nums:
            if votes == 0:
                candidate = num
            votes += 1 if num == candidate else -1
        return candidate


if __name__ == '__main__':
    n = [2,2,1,1,1,2,2]  # 2
    sol = Solution2()
    res = sol.majorityElement(n)
    print(f'Result --> {res}')  