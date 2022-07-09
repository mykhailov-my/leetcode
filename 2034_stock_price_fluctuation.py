"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
    max -> O(1)
    min -> O(1)
    current -> O(1)
    update -> O(Log N)
Space complexity -> O(N)

Solution
1. Initiate dict to store timestmp -> value, list of sorted values, ts value to store latest
2. for update
    1. if this ts is present in dict -> find an old price in list and delete value
    2. assign ts to dict
    3. update latest ts
    4. find a place via bisearch and insert value
3. current -> return from dict value by key of latest ts
4. max/min -> return begin/end of list
"""


from bisect import bisect_left

class StockPrice:

    def __init__(self):
        self.stocks = {}
        self.values = []
        self.latest_ts = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.stocks:
            ind = bisect_left(self.values, self.stocks[timestamp])
            del self.values[ind]
        self.stocks[timestamp] = price
        self.latest_ts = max(self.latest_ts, timestamp)
        ind = bisect_left(self.values, price)
        self.values.insert(ind, price)

    def current(self) -> int:
        return self.stocks[self.latest_ts]

    def maximum(self) -> int:
        return self.values[-1]

    def minimum(self) -> int:
        return self.values[0]


if __name__ == '__main__':
    n = ...
    sol = StockPrice()
    sol.update(1, 10)
    sol.update(2, 5)
    _ = sol.current()
    print(_)
    _ = sol.maximum()
    print(_)
    sol.update(1, 3)
    _ = sol.maximum()
    print(_)
    sol.update(4, 2)
    _ = sol.minimum()
    print(_)
