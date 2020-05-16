class Node:
  def __init__(self, v):
    self.val = v
    self.left = self.right = None

class BinarySearchTree():
  def __init__(self, node):
    self.root = node

  def insert(self, val):
    def insertHelper(val, node):
      if node.val < val:
        if node.right:
          return insertHelper(val, node.right)
        node.right = Node(val)
      elif node.val == val:
        return False
      else:
        if node.left:
          return insertHelper(val, node.left)
        node.left = Node(val)
      return True
    return insertHelper(val, self.root)

  def search(self, val):
    def searchHelper(self, val, node):
      if node == None:
        return
      if node.val == val:
        return node
      if val > node.val:
        return searchHelper(val, node.right)
      return searchHelper(val, node.left)
    return searchHelper(val, self.root)

  def predecessor(self, node):
    if not node:
      return None
    stack = []
    cur = self.root
    while cur and cur.val != node.val:
      if cur.val > node.val:
        stack.append(cur)
        cur = cur.left
      else:
        stack.append(cur)
        cur = cur.right
    if not stack:
      return None
    parent = cur
    while stack and parent.right != cur:
      cur = parent
      parent = stack.pop()
    if parent.right == cur:
      return parent
    return None

  def successor(self, node):
    if not node:
      return None
    if node.right:
      succ = node.right
      while succ.left:
        succ = succ.left
      return succ
    stack = []
    cur = self.root
    while cur and cur.val != node.val:
      if cur.val > node.val:
        stack.append(cur)
        cur = cur.left
      else:
        stack.append(cur)
        cur = cur.right
    if not stack:
      return None
    parent = cur
    while stack and parent.left != cur:
      cur = parent
      parent = stack.pop()
    if parent.right == cur:
      return parent
    return None      

  def getMinNode(self):
    cur = self.root
    if not cur:
      return None
    while cur.left:
      cur = cur.left
    return cur

  def getMaxNode(self):
    cur = self.root
    if not cur:
      return None
    while cur.right:
      cur = cur.right
    return cur

  def printTree(self, node):
    if not node:
      print("[ X ]")
      return
    print('[',node.val,']')
    self.printTree(node.left)
    self.printTree(node.right)


def main():
  bst = BinarySearchTree(Node(5))
  for i in range(1,10):
    bst.insert(i)

  bst.printTree(bst.root)
  pmin = bst.predecessor(bst.successor(bst.getMinNode()))
  print(pmin.val) if pmin else print('None')
  pmax = bst.predecessor(bst.getMaxNode())
  print(pmax.val) if pmax else print('None')

if __name__=="__main__":
  main()

