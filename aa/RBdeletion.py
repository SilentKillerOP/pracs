class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 1  # 1 for red, 0 for black

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        z = Node(key)
        z.parent = z.left = z.right = self.nil
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        if z.parent == None:
            z.color = 0
            return
        if z.parent.parent == None:
            return
        self.fix_insert(z)

    def fix_insert(self, z):
        while z.parent.color == 1:
            if z.parent == z.parent.parent.right:
                u = z.parent.parent.left  # uncle
                if u.color == 1:
                    u.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)
            else:
                u = z.parent.parent.right  # uncle
                if u.color == 1:
                    u.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.right_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = 0

    def find_node(self, key):
        x = self.root
        while x != self.nil:
            if key == x.data:
                return x
            elif key < x.data:
                x = x.left
            else:
                x = x.right
        return None

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.nil:
            node = node.right
        return node

    def inorder_traversal(self, node):
        if node != self.nil:
            self.inorder_traversal(node.left)
            print(str(node.data) +'R' if node.color else  str(node.data) +'B' , end=" ")
            self.inorder_traversal(node.right)

tree = RedBlackTree()

tree.insert(9)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.inorder_traversal(tree.root)
print()
tree.insert(1)
tree.insert(7)
tree.insert(20)
tree.inorder_traversal(tree.root)
print()
tree.insert(88)
tree.inorder_traversal(tree.root)