import numpy as np

class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, points):
        self.root = self.build_kdtree(points)

    def build_kdtree(self, points, depth=0):
        n = len(points)
        if n <= 0:
            return None

        axis = depth % len(points[0])
        sorted_points = points
        mid = n // 2

        return Node(
            sorted_points[mid],
            axis,
            left=self.build_kdtree(sorted_points[:mid], depth + 1),
            right=self.build_kdtree(sorted_points[mid + 1:], depth + 1),
        )

def print_inorder(node):
    if node is not None:
        print_inorder(node.left)
        print(node.point)
        print_inorder(node.right)




points = np.array([(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)])
kdtree = KDTree(points)

print_inorder(kdtree.root)