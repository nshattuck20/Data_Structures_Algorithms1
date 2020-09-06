from ch12.DoublyLinkedLists.LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        self.list.append(new_item) # Insert as list tail (end of queue)

    def pop(self):
        popped_item = self.list.head # Copy of list head (front of the queue)
        self.list.remove_after(None) # Remove list head
        return popped_item # Return popped item



