from binary_tree import BinaryTree

r = BinaryTree('a')

r.insert_left('left')
print(r.get_left_child().get_root_value())