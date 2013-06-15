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
            
    # pre:  format and filter are optional functions which are applied to each node's children
    # post: returns the html for a single noed
    def write(self, format=None, _filter=None):
        html = "<" + self.tag + ">"
        if _filter:
            self.children = filter(_filter, self.children)
        for child in self.children:
            if child.tag == "text":
                html += child.value
            elif format:
                html += format(child.write())
            else:
                html += child.write()
        if self.selfClosing:
            return html
        else:
            return html + "</" + self.tag + ">"

class Tree:
    def __init__(self, root=None):
        self.root = root

    def printRoot(self):
        self.root.printNode()

    def write(self, format=None, _filter=None):
        return self.root.write(format, _filter)
