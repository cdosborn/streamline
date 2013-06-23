Priority
---
* Update comment syntax (adt.py as example)
* Increase parse robustness (trouble sites)
    * http://maryrosecook.com/post/when-i-died-2
         * It would seem that the parser is having issues handling the comment at line 256.
* Write some filter functions
    * node with max # of p tags
* Node class should be simplified

Ongoing
---
* Add TESTS!!
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
* Enable handling of self closing tags
* Modify streamline to incorporate changes
