# Abstract data types
# -------------------

class Node:
    def __init__(self, tag, value=None, selfClosing=None):
        self.tag = tag
        self.children = []
        self.value = value
        self.selfClosing = selfClosing;

    def printNode(self, indent=""):
        print indent + "tag: " + self.tag
        if self.value:
            print indent + "value: " + self.value
        print indent + "children:"
        for child in self.children:
            child.printNode(indent + "    ")

    def addChild(self, child):
        self.children.append(child)
    
    def addNoClosingChild(self, tag):
        self.addChild(Node(tag,None,True))

    def addTextChild(self, text):
        if text != "":
            self.addChild(Node("text",text))

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
            elif format:
                cumhtml += format(self._explore(child))
            else:
                cumhtml += self._explore(child)
        if node.selfClosing:
            return cumhtml
        else:
            return cumhtml + "</" + node.tag + ">"
