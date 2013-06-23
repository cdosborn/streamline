class Node:
    # selfClosing | bool
    # value, tag  | str
    # Node        | fn(str,str,bool) -> Node, constructs a leaf node
    def __init__(self, tag, value=None, selfClosing=False):
        self.tag = tag
        self.children = []
        self.value = value
        self.selfClosing = selfClosing;

    # printRoot | None, prints node to console
    def printNode(self, indent=""):
        print indent + "tag: " + self.tag
        if self.value:
            print indent + "value: " + self.value
        print indent + "children:"
        for child in self.children:
            child.printNode(indent + "    ")

    # child    | Node
    # addChild | fn(Node) -> None, adds node as child
    def addChild(self, child):
        self.children.append(child)
        
    # tag               | str
    # addNoClosingChild | fn(str) -> None, adds self-closing child
    def addNoClosingChild(self, tag):
        self.addChild(Node(tag,None,True))

    # text         | str
    # addTextChild | fn(str) -> None, adds child to self with value text
    def addTextChild(self, text):
        if text != "":
            self.addChild(Node("text",text))
            
    # select | fn(node) -> bool, returns whether a node should be written
    # indent | fn(str) -> str, apply indent/style to source html
    # write  | fn(fn,fn) -> str, returns the node as html
    def write(self, indent=None, select=None):
        html = "<" + self.tag + ">"
        if select:
            self.children = filter(select, self.children)
        for child in self.children:
            if child.tag == "text":
                html += child.value
            elif indent:
                html += indent(child.write())
            else:
                html += child.write()
        if self.selfClosing:
            return html
        else:
            return html + "</" + self.tag + ">"

class Tree:
    # root | Node
    # Tree | fn(Node) -> Tree, returns tree with a reference to root
    def __init__(self, root=None):
        self.root = root

    # printRoot | None, prints tree to console
    def printRoot(self):
        self.root.printNode()

    # select | fn(Node) -> bool, returns whether a node should be written
    # indent | fn(str) -> str, apply indent/style to source html
    # write  | fn(fn,fn) -> str, returns the given tree as html
    def write(self, select=None, indent=None):
        return self.root.write(indent, select)

    # tag | str
    # get | fn(str) -> str, retrieves node or first child with matching tag
    def get(self, tag):
        return self._get(tag, self.root)

    # tag  | str
    # node | Node
    # _get | fn(str, Node) -> str, retrieves node or first child with matching tag
    def _get(self, tag, node):
        if node.tag == tag:
            return node
        for child in node.children:
            if child.tag == tag:
                return child
        for child in node.children:
            return self._get(tag, child)   

#    def grabContent(self):
#        ''' 
#        if not contains p tag
#            explore children
#        (directly) contains p tag
#            how many p tag    
#        '''  
