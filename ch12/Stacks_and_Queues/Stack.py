from ch12.DoublyLinkedLists.LinkedList import LinkedList
class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        self.list.prepend(new_item) # Insert list at the top of the stack

    def pop(self):
        popped_item = self.list.head    # Copy list head (top of stack)
        self.list.remove_after(None)    # Remove head of list
        return popped_item              # Return popped item


