# Solved by myself
# Time complexity O(n)
# Space complexity O(1)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1 if n else 0
        while (n > 0):
            last_digit = n % 10
            sum += last_digit
            product *= last_digit
            n = int(n / 10)
        return product - sum

if __name__ == '__main__':
    n = 1
    sol = Solution()
    res = sol.subtractProductAndSum(n)
    print(f'Result --> {res}')