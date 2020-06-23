class Node:
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self, val):
    node = Node(val)
    if self.root == None:
      self.root = node
    else:
      current_node = self.root
      while(True):
        if self.root.val < val:
          if self.root.right == None:
            self.root.right = node
            break
          current_node = self.root.right
        else:
          if self.root.left == None:
            self.root.left = node
            break
          current_node = self.root.left
  
  def look_up(self, val):
    current_node = self.root
    while(current_node):
      if current_node.val == val:
        return current_node
      elif current_node.val < val:
        current_node = current_node.right
      elif current_node.val > val:
        current_node = current_node.left
    return False

def treverse(root): 
  if root: 
    treverse(root.left) 
    print(root.val) 
    treverse(root.right) 

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
# tree.insert(6)
tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# tree.insert(1)
treverse(tree.root)
print(tree.look_up(10))
