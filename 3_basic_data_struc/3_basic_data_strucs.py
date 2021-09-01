# stacks
#
# sometimes called a push-down stack
#
# ordered collection of items where the addition of new items and
# the removal of existing items always takes place at the same end.
#
# last-in first-out
# newer items are always at the top older items at the base

stack()  # creates a new stack that is empty
push(item)  # adds item to the top of the stack
pop()  # removes the top item from the stack
peek()  # returns the top item from the stack but doesnt remove it
isEmpty()  # test to see whether the stack is empty
size()  # returns number of items in stack


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Balanced Parenthesis
# import the above stack class
def par_checker(symbol_string):
    s = stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens, closers = '([{', ')]}'

    return opens.index(open) == closers.index(close)

print(par_checker('({[]})'))