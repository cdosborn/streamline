Priority
---
* trees implement a get method, we need nodes to implement it as well or we get the awkward situation in streamline.py when we have to make two trees
* increase parse robustness (trouble sites)
* write some filter functions
    * node with max # of p tags
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
* parse.py + streamline.py need to be refactored and simplified
* parser couldn't handle tags outside surrounding html (http://maryrosecook.com/post/when-i-died-2)
* enable handling of self closing tags
* modify streamline to incorporate changes
