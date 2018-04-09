"""
Solution for Quesiton Three of the Junior DevOps Codility Test.
Note: The Codility test provided a library (TreeNode?) which provides traversal "for free"
but I use my own simple class here.
"""

class TreeNode():
    """TreeNode is the root of the tree."""

    def __init__(self, val, left=None, right=None, parent=None):
        """."""
        self.val = val
        self.left = left
        self.right = right

    def children(self):
        """Return non-none children of node."""
        return [n for n in [self.left, self.right] if n is not None]


class BT():
    """Instantiate a Binary Tree Object."""
    def __init__(self):
        self.root = None


    def post_order(self, root='root'):
        """
        Yield a node by visiting left child, then the right child and then
        the parent.
        """
        if root == 'root':
            root = self.root
        if root:
            for node in root.children():
                for node in self.post_order(root=node):
                    yield node
            yield root


def solution(T):
    """Return the number of minimum unique value in any path from root to leaf."""
    pass
