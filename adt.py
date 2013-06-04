# Abstract data types
# -------------------

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

class Tree:
    def __init__(self, root=None):
        self.root = root

    def printRoot(self):
        self.root.printNode()

    def write(self, format=None, filter=None):
        return self._explore(self.root)

    def _explore(self, node, format=None, filter=None): # test at the bottom
        cumhtml = "<" + node.tag + ">"
        if filter:
            node.children = filter(node.children)
        for child in node.children:
            if child.tag == "text":
                cumhtml += child.value
            else:
                if format:
                    cumhtml += format(self._explore(child))
                else:
                    cumhtml += self._explore(child)
        return cumhtml + "</" + node.tag + ">"
