Priority
---
* node class needs to support attributes (class,id,href)
* get method extended such that tree.get("div","class","id")
* filter functions
    * blacklist (script,style,etc)
    * node with max # of p tags
* resolve text nodes, I don't like that the tag is set to "text"
* code in script tags sometimes interpreted as text nodes 
* trees implement a get method, which needs to be implemented by the node class
* regex doesn't handle nested comments (<!-- <!-- --> should be comment -->)
* node class should be simplified


Ongoing
---
* Update comment syntax (adt.py as example)
* add TESTS!!
    * The regex in parse!
        * self-closing (br, em, link)
        * comments (which contain tags)
        * script tags 
    * closingTag (self-closing tag)
    * Tree.write
    * Doc.py
    * Streamline.py

Completed
---
* tree.get actually scans correctly now :D
* parse.py + streamline.py need to be refactored and simplified
* parser couldn't handle tags outside surrounding html (http://maryrosecook.com/post/when-i-died-2)
* enable handling of self closing tags
* modify streamline to incorporate changes
