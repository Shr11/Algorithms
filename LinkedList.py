#single node
class Node:                                              

  # constructor
    def __init__(self, data : int,next_node = None):
        self.data=data
        self.next=next_node

class LL:        
 #linked list with single head node
   def __init__(self):
        self.head= None

   def insert(self, data ):       
         # insertion method for linked list
        newNode = Node(data)

        if(self.head):
         temp = self.head
         while(temp.next):
            temp=temp.next
         temp.next = newNode

        else:
           self.head=newNode

          #printing Linked List 
   def printLL(self):
           temp=self.head
           while(temp):
              print(temp.data)
              temp= temp.next   

#inserting and printing a linked list
L=LL()


L.insert(3)
L.insert(4)
L.insert(5)
L.printLL()