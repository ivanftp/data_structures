
# Preorder traversal (left, root, right)
# Visit root node first
# Then recursively do a preorder traversal of the left subtree
# followed by a recursive preorder traversal of the right subtree
# reading a book from 1st chapter onwards

# Inorder traversal (root, left, right)
# Recursively do an inorder traversal on the left subtree,
# visit the root node,
# finally do a recursive inorder traversal of the right subtree

# Postorder (left, right, root)
# Recursively do a postorder traversal of the left subtree and the right subtree
# followed by a visit to the root node


class BinaryTree(object):

    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, object):
        self.key = object

    def get_root_value(self):
        return self.key


if __name__ == "__main__":
    tree1 = BinaryTree(1)
    tree2 = BinaryTree(2)
    tree2.insert_left(4)
    tree2.insert_right(5)

    tree1.left_child = tree2
    tree1.insert_right(3)

    print(tree1.get_root_value())
    print(tree1.get_left_child().get_root_value())
    print(tree1.get_left_child().get_left_child().get_root_value())
    print(tree1.get_left_child().get_right_child().get_root_value())
    print(tree1.get_right_child().get_root_value())
