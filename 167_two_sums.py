class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        small = 0
        big = len(numbers) - 1
        while small < big:
            sum = numbers[small] + numbers[big]
            if sum > target:
                big -= 1
            elif sum == target:
                return [small + 1, big + 1]
            else:
                small += 1
            

if __name__ == '__main__':
    n = [2, 3, 4]
    target = 6
    sol = Solution()
    res = sol.twoSum(n, target)
    print(f'Result --> {res}')