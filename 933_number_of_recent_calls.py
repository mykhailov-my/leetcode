

from bisect import bisect_left


class RecentCounter:
    """
    Status -> Solved by myself

    Tags -> Binary search

    Time complexity -> O(Log N)
    Space complexity -> O(N)

    """

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        start = bisect_left(self.requests, t - 3000)
        return len(self.requests) - start


if __name__ == '__main__':
    sol = RecentCounter()
    res = sol.fuRecentCounternc(1)
    print(f'Result --> {res}')
    res = sol.fuRecentCounternc(100)
    print(f'Result --> {res}')
    res = sol.fuRecentCounternc(3001)
    print(f'Result --> {res}')
    res = sol.fuRecentCounternc(3002)
    print(f'Result --> {res}')