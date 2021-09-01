from binary_tree import BinaryTree
import operator


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = []
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insert_left('')
            pStack.append(currentTree)
            currentTree = currentTree.get_left_child()

        elif i in ['+', '-', '*', '/']:
            currentTree.set_root_value(i)
            currentTree.insert_right('')
            pStack.append(currentTree)
            currentTree = currentTree.get_right_child()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.set_root_value(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


def evaluate(parse_tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operators[parse_tree.get_root_value()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_value()



pt = buildParseTree("( ( 10 + 5 ) * 3 )")
preorder(pt)
#pt.postorder()  # defined and explained in the next section
