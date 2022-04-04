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
             self.tail.next = node      # if list is not empty, (head/tail same for first value,so we use tail so that later tail is updated for every value)
             node.prev = self.tail      # we have to say what is the previous value of the node 
             self.tail = node           # tail would be new node 
             self.size +=1 



    # (1  2  3 4 5) remove 3. update 2's next is 4 and 4's prev is 2
    def __remove_node(self,node):
        if node.prev is None:
            self.head = node.next       # if we are in head and if we remove it, we update the head 
        else :
            node.prev.next = node.next  # changed the prev node's node.next pointer (updated the next element) 2's next is 4
        
        if node.next is None:
            self.tail = node.prev       # if we are in tail and if we remove it, we update the tail 
        else:
            node.next.prev = node.prev  # changed the next node's node.prev pointer (updated prev element) 4's prev is 2
        self.size -=1

    def remove(self,value):
        node = self.head                #temporary node is self.head,we will search the value from the head
        while node is not None:
            if node.val==value:
                self.__remove_node(node)
                break
            node = node.next 
    
    # this function is for printing the linked list. !important, we are here to learn ds algo          
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
my_list.add(4)


print(my_list)
print('size : ',my_list.size)

my_list.remove(4)
print(my_list)
print('size : ',my_list.size)
