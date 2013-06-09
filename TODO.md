Priority
---
* NOTHING MORE UNTIL TESTS (tests need documentation also)
    * The regex in parse!
        * self-closing (br, em, link)
        * comments (which contain tags)
        * script tags 
    * closingTag (self-closing tag)
    * Tree.write
    * Doc.py
    * Streamline.py

* Increase parse robustness
* Write some filter functions
    * node with max # of p tags
* In node class, adding children needs consistency should all the add children methods just take a tag? Notice how addChild is a helper for the other two.


Ongoing
---
* Add TESTS!!

Completed
---
* Enable handling of self closing tags
* Modify streamline to incorporate changes
