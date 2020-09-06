from ch12.DoublyLinkedLists.LinkedList import LinkedList
from ch12.DoublyLinkedLists.Node import Node
from ch12.Stacks_and_Queues.Stack import Stack
from ch12.Stacks_and_Queues.Queue import Queue

#######Stack########
num_stack = Stack()

node_a = Node(44)
node_b = Node(99)
node_c = Node(1)

num_stack.push(node_a)
num_stack.push(node_b)
num_stack.push(node_c)

# Output
print('Stack after push', end=' ')
node = num_stack.list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

popped_item = num_stack.pop() # Pop node_c
print('Stack after pop:', end = ' ')
node = num_stack.list.head
while node != None:
    print(node.data, end =' ')
    node = node.next
print()


#####Queue#######
num_queue = Queue()

node_1 = Node(77)
node_2 = Node(22)
node_3 = Node(0)

num_queue.push(node_1)
num_queue.push(node_2)
num_queue.push(node_3)

# Output after pushing ot the Queue
print('Queue after push:', end=" ")
node = num_queue.list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

popped_item = num_queue.pop() # Remove node_1
# Output after popping from Queue
print('Queue after popping:', end=' ')
node = num_queue.list.head
while node != None:
    print(node.data, end = ' ')
    node = node.next
print()


