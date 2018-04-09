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
    """
    Return the maximum number of unique values in any path from root to leaf.
    We first find all the leaves of the left subtree by post_order traversal and
    keep track if a node is on the path and track it's value
    """
    paths = defaultdict(lambda: ([], []))
    path = []
    for n in bt.post_order():
        for child in n.children():
            label, value = child.val
            if label in paths.keys():
                unique_vals = paths[label][0]
                if n.val[1] not in unique_vals:
                    paths[label][0].append(n.val[1])
                paths[label][1].append(n)
            else:
                for k, v in paths.items():
                    unique_vals, nodes_in_path = v
                    if child == nodes_in_path[-1]:
                        if n.val[1] not in unique_vals:
                            paths[k][0].append(n.val[1])
                        paths[k][1].append(n)

        # add node id / label to dict to start keeping track of unique values and nodes encountered on the path
        if n.is_leaf():
            unique_vals, nodes_in_path = paths[n.val[0]]
            if n.val[1] not in unique_vals:
                unique_vals.append(n.val[1])
                nodes_in_path.append(n)
                paths[n.val[0]] = (unique_vals, nodes_in_path)

        length_unique_vals_per_path = []
        for k, v in paths.items():
            unique_vals, nodes_in_path = v
            length_unique_vals_per_path.append(len(unique_vals))

    return(max(length_unique_vals_per_path))
