class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next
    print('-------------------------')
  
  def printListRev(self):
    temp = self.tail
    while(temp):
      print(temp.data)
      temp = temp.prev 
  
  def prepend(self, data):
    new_node = Node(data)
    self.head.prev = new_node
    new_node.next = self.head
    self.head = new_node
  
  def append(self, data):
    new_node = Node(data)
    self.tail.next = new_node
    new_node.prev = self.tail
    self.tail = new_node
  
  def insert(self, data, index):
    temp = self.head
    for i in range(index):
      temp = temp.next
    hold_prev = temp.prev
    new_node = Node(data)
    hold_prev.next = new_node
    temp.prev = new_node
    new_node.prev = hold_prev
    new_node.next = temp
  
  def delete(self, index):
    temp = self.head
    for i in range(index):
      temp = temp.next
    temp.prev.next = temp.next
    temp.next.prev = temp.prev

    
if __name__=='__main__':
  llist = LinkedList()
  llist.head = Node(1)
  second = Node(2)
  llist.tail = Node('-')
  llist.head.next = second
  second.next = llist.tail
  llist.tail.prev = second
  second.prev = llist.head
  llist.prepend(0)
  llist.append(4)
  llist.insert(3,3)
  llist.delete(4)
  llist.printList()
  llist.printListRev()
