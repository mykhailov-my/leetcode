

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self, depth=1) -> str:
        left_str = self.left.__str__(depth + 1) if self.left else ''
        right_str = self.right.__str__(depth + 1) if self.right else ''
        s = f'({self.val}) -> \n' + ('  ' * depth) + f'{left_str} \n' + ('  ' * depth) +f'{right_str}'
        return s

    def __repr__(self) -> str:
        return self.__str__()

def create_bi_tree(values, previous=None, start=1):
    if previous is None:
        previous = [TreeNode(values[0])]
    elif previous == []:
        return None
        # start = 1
    if start >= len(values):
        return None
    next_nodes = []
    for prev_node in previous:
        l = TreeNode(values[start])
        r = TreeNode(values[start + 1])
        prev_node.left = l
        prev_node.right = r
        next_nodes.append(l)
        next_nodes.append(r)
        start += 2
        # breakpoint()
    
    create_bi_tree(values, next_nodes, start)
    if len(previous) == 1:
        return previous[0]
    



class Solution:
    """
    Status -> Solved by myself

    Tags -> Tree, Binary Tree

    Time complexity -> O(N)
    Space complexity -> O(H) , h is tree height 


    Notes 
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



if __name__ == '__main__':
    n = create_bi_tree([4, 2,7, 1,3,6,9])
    sol = Solution()
    res = sol.invertTree(n)
    print(f'Result --> {res}')  

