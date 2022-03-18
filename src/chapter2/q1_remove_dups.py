# Write code to remove duplicates from an un-sorted linked list
from CTCIPythonPlayground.src.utils.LinkedList import LinkedList, Node


class Q1RemoveDups(LinkedList):

    def remove_dups(self):
        curr, prev = self.head, self.head
        list_dict = {}
        while curr is not None:
            list_dict[curr.val] = True
            curr = curr.next
            prev.next = None

        self.head = None
        for val in list_dict:
            self.add(val)
