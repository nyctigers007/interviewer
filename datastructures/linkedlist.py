# list implementation
# single linked list
#
class Node(object):
    def __init__(self,val):
        self.data = val
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None

    def push(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode


    def insertAfter(self, prev, new_data):
        newnode = Node(new_data)
        temp = self.head
        newnode.next = prev.next
        prev.next = newnode

    def append(self,new_data):
        if self.head is None:
            self.head = Node(new_data)

        temp = self.head
        while (temp.next):
            temp =temp.next

        temp.next = Node(new_data)

    def delete(self, val):
        if self.head is None:
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        temp = self.head

        while(temp.next):
            if temp.next.data == val:
                break

        temp.next = temp.next.next

        return


    def printList(self):
        temp = self.head
        while temp:
            print 'printing node data:', temp.data
            temp = temp.next

ll = linkedList()
ll.push(1)
ll.push(4)
ll.push(32)
ll.push(12)
ll.printList()
prev = Node(Node(12))
ll.insertAfter(ll.head.next.next, 10000)
ll.printList()
ll.append(2000)
print 'appending 2000'
ll.printList()
print 'deleting 32'
ll.delete(32)
ll.printList()

# double linked list
class Node (object):
    def __init__(self, prev=None, next=None, val= None):
        self.next = next
        self.prev = prev
        self.data = val


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    def push(self,new_val):
        # make the new node
        newnode = Node(val=new_val)
        newnode.next = self.head
        newnode.prev = None

        if self.head is not None:
            self.head.prev = newnode

        self.head = newnode

    def insertAfter(self, prevnode, data):
         if prevnode is None:
             return

         newnode = Node(val=data)

         newnode.next = prevnode.next  # node after
         newnode.prev = prevnode

         prevnode.next = newnode

         # newnode.next(the node after)
         if newnode.next is not None:
             newnode.next.prev = newnode


    def append(self,val):
         newnode = Node(prev=None, next=None,val=val)
         temp = self.head

         if self.head is None:
             self.head = newnode
             return

         while (temp.next):
             temp=temp.next

         temp.next = newnode
         newnode.prev = temp


    def insertBefore(self, node, val):
         if node is None:
             return

         newnode = Node(prev=None,next=None, val=val)

         newnode.next = node
         newnode.prev = node.prev
         node.prev.next = newnode

         node.prev=newnode


    def printList(self):
         if self.head is None:
             return

         temp = self.head

         while (temp):
             print temp.data
             temp = temp.next

dlist = DoubleLinkedList()
dlist.append(6)
dlist.push(7)
dlist.push(1)
dlist.append(4)
print 'print before insert after'
dlist.printList()
dlist.insertAfter(dlist.head.next,8)
print 'after insert after'
dlist.printList()


