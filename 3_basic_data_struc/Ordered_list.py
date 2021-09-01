from Node import Node


class OrderedList:

    def __init__(self):
        self.head = None

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

    def get_head(self):
        return self.head.get_data()

    def is_empty(self):
        return self.head is None

    def length(self):
        current, count = self.head, 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current, found, stop = self.head, False, False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current, previous, stop = self.head, None, False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous, current = current, current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
