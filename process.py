import re
import tree
from parser import parse

def grab(tag, html): #
    opentag = "<" + tag + ">"
    endtag = "</" + tag + ">"
    start = html.find(opentag)
    end = html.find(endtag)
    return html[start:end + len(endtag)]
    
def write(node, taglist):
    html = explore(node)
    # taglist = ["title", "h1", "p"]
    readyHtml = ""
    for item in taglist:
        readyhtml += grab(item)
    return readyhtml

def explore(node): # test at the bottom
    cumhtml = ""
    for child in node.children:
        if child.tag == "text":
            cumhtml += child.value
        else:
            opentag = "<" + child.tag + ">"
            endtag = "</" + child.tag + ">"
            cumhtml += "\n" + opentag + explore(child) + endtag + "\n"
    return cumhtml

#perhaps add functionality to ignore tags
html = "<html headasdfa df ><p><p><span title=\"span\">I'm a nested span</span></p></p></html>"
print html
tree = tree.Tree(parse(html))
testhtml = explore(tree.root)
tree.root.printNode()
print testhtml

