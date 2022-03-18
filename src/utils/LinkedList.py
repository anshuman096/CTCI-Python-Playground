class Node:
    def __init__(self, node_val=None):
        self.val = node_val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def print_list(self):
        if self.head is None:
            print('[]')
        else:
            list_str = '['
            curr = self.head
            while curr is not None:
                list_str += (str(curr.val) + ' -> ')
                curr = curr.next
            list_str += 'None]'
            print(list_str)
            return list_str
