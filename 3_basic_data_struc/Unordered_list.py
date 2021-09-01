from Node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head.get_data()

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        current, count = self.head, 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current, found = self.head, False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current, previous, found = self.head, None, False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous, current = current, current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
