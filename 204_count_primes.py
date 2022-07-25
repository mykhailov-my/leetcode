"""
Status -> Solved with hint


Not allowed solution (code is too big)
1 pre-calculate all primes to 10^6
2 bin search value
3 return index + 1

"""

class Solution1:
    '''
    Too slow, Time Limit Exceeded
    '''
    def countPrimes(self, n: int) -> int:
        primes = []
        for i in range(2, n):
            if all(i % p != 0 for p in primes):
                primes.append(i)
        return len(primes)

class Solution2:
    '''
    Solved with hint

    1. create list full of nums with len N
    2. iterate from 2 to N
    3. if list[i] marked as False -> it's already non prime, continue
    4. else -> this num is prime, mark current index as True
    5. iterate from i^2 to n with step of i and mark values to False
    6. return count of True values in list

    Time complexity -> O(N)?
    Space complexity -> O(N)
    '''
    def countPrimes(self, n: int) -> int:
        nums = [None] * n
        for i in range(2, n):
            if nums[i] == False:
                continue
            nums[i] = True
            for j in range(i**2, n, i):
                nums[j] = False
        return nums.count(True)

if __name__ == '__main__':
    n = 10
    sol = Solution2()
    res = sol.countPrimes(n)
    print(f'Result --> {res}')  