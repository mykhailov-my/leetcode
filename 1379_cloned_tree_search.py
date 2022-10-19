
class Solution:
    """
    Status -> Solved by myself

    Tags -> BFS

    Time complexity -> O(V+E)
    Space complexity -> O(V)

    Solution -> BFS


    Notes 
    """
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned.val == target.val:
            return cloned
        visited = {cloned}
        queue = [cloned]
        while queue:
            s = queue.pop()
            for adjacent in (s.left, s.right):
                if adjacent is None:
                    continue
                if adjacent.val == target.val:
                    return adjacent
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)



if __name__ == '__main__':
    n = ...
    sol = Solution()
    res = sol.func(n)
    print(f'Result --> {res}')  