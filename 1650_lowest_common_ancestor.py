

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    """
    Status -> Solved by myself

    Tags -> Binary tree

    Time complexity -> O(H)
    Space complexity -> O(H)

    Solution
    1. Create list of all parents for one node
    2. Iterate parents of second node if parent in list of first parent -> return node

    Notes 
    """
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = {p.val}
        while p.parent != None:
            p = p.parent
            p_ancestors.add(p.val)
        # print(p_ancestors)
        
        while q != None:
            # print(q.val)
            if q.val in p_ancestors:
                return q
            q = q.parent
        return None


if __name__ == '__main__':
    n = ...
    sol = Solution()
    res = sol.lowestCommonAncestor(n)
    print(f'Result --> {res}')  