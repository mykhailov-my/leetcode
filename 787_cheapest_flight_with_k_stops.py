
from collections import deque


class Solution:
    """
    Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

    Tags ->

    Time complexity ->
    Space complexity ->

    Solution
    1.
    2.
    3.

    Notes 
    """
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for from_, to, price in flights:
            nodes = graph.get(from_, [])
            nodes.append((to, price))
            graph[from_] = nodes
        print(graph)
        if src not in graph:
            return -1
        queue = deque()
        queue.append(src)
        queue.append(-1)
        path = {src: 0}
        stops = 0
        min_price = float('inf')

        while queue and stops <= k:
            print(f'Q {queue} \tP {path} \tS {stops}')
            node = queue.popleft()
            if node == -1:
                stops += 1
                if queue:
                    queue.append(-1)
            else:
                for link in graph.get(node, []):
                    adjacent_node, price = link
                    if adjacent_node not in path:
                        queue.append(adjacent_node)
                        if adjacent_node == dst:
                            print(f'Price changed to {min(price + path[node], min_price)}')
                            min_price = min(price + path[node], min_price)
                        else:
                            # breakpoint()
                            path[adjacent_node] = price + path.get(node, 0)
        return min_price


if __name__ == '__main__':
    n = 4  # 700
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1

    n = 2
    flights = [[0,1,2],[1,2,1],[2,0,10]]
    src = 1
    dst = 2
    k = 1

    n = 15  # 169
    flights = [[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]]
    src = 1
    dst = 4
    k = 10
    sol = Solution()
    res = sol.findCheapestPrice(n, flights, src, dst, k)
    print(f'Result --> {res}')  