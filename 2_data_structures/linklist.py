class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next_value):
        self.next = next_value


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, value):
        item = self.head

        while item != None:
            if item.get_data() == value:
                return item
            else:
                item = item.get_next()

        return None

    def delete_at(self, index):
        if index > self.count - 1:
            return

        if index == 0:
            self.head = self.head.get_next()
        else:
            temporary_index = 0
            node = self.head

            print(node, temporary_index, self.head)

            while temporary_index < index - 1:

                node = node.get_next()
                temporary_index += 1

            node.set_next(node.get_next().get_next())

            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while tempnode != None:
            print("node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


itemlist = LinkedList()

for i in range(10, 20, 2):
    itemlist.insert(i)


itemlist.dump_list()

# Exercise the list
print("Before deleting ....")
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(15)) # Should be None
print("Finding item", itemlist.find(12))   # Should be a node object

# Delete an item

itemlist.delete_at(itemlist.count - 2)

print("After deleting ....")
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(12)) # Should be None

itemlist.dump_list()