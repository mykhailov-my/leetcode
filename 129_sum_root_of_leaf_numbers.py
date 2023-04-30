from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    """
    Status -> Solved by myself

    Tags -> Binary tree, DFS

    Time complexity -> O(log N)
    Space complexity -> O(log N)

    Solution
    1. use dfs. build prefix (multiply by 10 and add val)
    2. if node is leaf (no left and right) add prefix to counter

    Notes 
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, prefix=0):
            if node is None:
                return
            new_prefix = prefix * 10 + node.val
            if node.left is None and node.right is None:
                nonlocal result
                result += new_prefix
            else:
                dfs(node.left, new_prefix)
                dfs(node.right, new_prefix)
        dfs(root)
        return result


def generate_testcase(l, pos=0):
    if pos >= len(l):
        return
    left = generate_testcase(l, pos*2+1)
    right = generate_testcase(l, pos*2+2)
    node = TreeNode(l[pos], left, right)
    return node


if __name__ == '__main__':
    root = generate_testcase([4,9,0,5,1])
    sol = Solution()
    res = sol.sumNumbers(root)
    print(f'Result --> {res}')