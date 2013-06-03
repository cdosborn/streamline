class Node:
  def __init__(self, tag, value=None):
    self.tag = tag
    self.children = []
    self.value = value

  def printNode(self, indent=""):
    print indent + "tag: " + self.tag
    if self.value:
        print indent + "value: " + self.value
    print indent + "children:"
    for child in self.children:
        child.printNode(indent + "    ")

  def addChild(self, child):
    self.children.append(child)

  def addTextChild(self, text):
      if text != "":
          self.children.append(Node("text",text))

'''
Tree and Node Class
-------------------
'''
class Tree:
  def __init__(self, root=None):
    self.root = root
  
  def printRoot(self):
    self.root.printNode()
