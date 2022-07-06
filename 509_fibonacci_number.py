"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. create list [0,1]
2. if n in list -> return l[n]
3. iterate from len l to n
4. append to list sum of two previous nums
"""

class Solution:
    l = [0, 1]
    def fib(self, n: int) -> int:
        if len(self.l) - 1 >= n:
            return self.l[n]
        for i in range(len(self.l), n + 1):
            self.l.append(self.l[i-1] + self.l[i-2])
        # print(self.l)
        return self.l[n]



if __name__ == '__main__':
    n = 7
    sol = Solution()
    res = sol.fib(n)
    print(f'Result --> {res}')  