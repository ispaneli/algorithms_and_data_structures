class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key


class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None)  # For splay()

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            raise Exception('key not found in tree')

        # Now delete the root.
        if self.root.left == None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None

    def splay(self, key):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t


s = SplayTree()

# elif new_root == new_root.parent.left and new_root.parent == new_root.parent.parent.left:
#     # Zig-Zig step.
#     self._right_rotation(new_root.parent.parent)
#     self._right_rotation(new_root.parent)
# elif new_root == new_root.parent.right and new_root.parent == new_root.parent.parent.right:
#     # Zag-Zag step.
#     self._left_rotation(new_root.parent.parent)
#     self._left_rotation(new_root.parent)
# elif new_root == new_root.parent.right and new_root.parent == new_root.parent.parent.left:
#     # Zig-Zag step.
#     self._left_rotation(new_root.parent)
#     self._right_rotation(new_root.parent)
# else:
#     # Zag-Zig step.
#     self._right_rotation(new_root.parent)
#     self._left_rotation(new_root.parent)


# tree = SplayTree()
# tree.add(8, "10")
# tree.add(4, "14")
# tree.add(7, "15")
# tree.set(8, "11")
# tree.add(3, "13")
# tree.add(5, "16")
# tree.search(88)
# tree.search(7)
# tree.delete(5)
# tree.print()
# 8 4 7 3 5


# while new_root.parent != None:
#     if new_root.parent.parent == None:
#         if new_root == new_root.parent.left:
#             # zig rotation
#             self._right_rotation(new_root.parent)
#         else:
#             # zag rotation
#             self._left_rotation(new_root.parent)
#     elif new_root == new_root.parent.left and new_root.parent == new_root.parent.parent.left:
#         # zig-zig rotation
#         self._right_rotation(new_root.parent.parent)
#         self._right_rotation(new_root.parent)
#     elif new_root == new_root.parent.right and new_root.parent == new_root.parent.parent.right:
#         # zag-zag rotation
#         self._left_rotation(new_root.parent.parent)
#         self._left_rotation(new_root.parent)
#     elif new_root == new_root.parent.right and new_root.parent == new_root.parent.parent.left:
#         # zig-zag rotation
#         self._left_rotation(new_root.parent)
#         self._right_rotation(new_root.parent)
#     else:
#         # zag-zig rotation
#         self._right_rotation(new_root.parent)
#         self._left_rotation(new_root.parent)
