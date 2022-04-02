# lets make a class for each node 
class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None  
# now lets make doubly linked list class 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 
    
    def add(self,val):
         node = Node(val) # created a node here
         # when we create a node, we have to update DoublyLinkedList class
         if self.tail is None:
             self.head = node 
             self.tail = node 
             self.size += 1 
             # when there is only one value, that will be head and tail 
         else:
             self.tail.next = node  # if list is not empty, (head/tail same for first value,so we use tail so that later tail is updated for every value)
             node.prev = self.head  # new node's previous , linked list head updated here
             self.tail = node       # tail would be new node 
             self.size +=1 
    
    # this function is for printing the linked list. !important, we are here to learn ds algo        self.size+= 1  
    def __str__(self):
        vals = []
        node = self.head 
        while node is not None:
            vals.append(node.val)
            node = node.next  
        return f"[{', '.join(str(val) for val in vals)}]"

my_list = DoublyLinkedList() 
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)

print(my_list)
