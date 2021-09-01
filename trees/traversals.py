def preorder(tree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


# inside class
# def preorder(self):
#     print(self.key)
#     if self.left_child:
#         self.left.preorder()
#     if self.right_child:
#         self.right.preorder()

def postorder(tree):
    if tree:
        postorder(tree.get_left_child)
        postorder(tree.get_right_child)
        print(tree.get_root_value)


def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())

        