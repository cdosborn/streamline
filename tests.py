import parser

print "TESTS: closingTag"
print str(parser.closingTag("adsfasdf", "p") == -1);
print str(parser.closingTag("<p adsfasdf></p>", "p") == len("<p adsfasdf>"))
print str(parser.closingTag("<p><p><p><p></p></p></p></p>", "p") == len("<p><p><p><p></p></p></p>"))
print str(parser.closingTag("<durp>asdfsd</durp>asd</durp>ad", "durp") == len("<durp>asdfsd"))
print ""

print "TESTS: textBeforeTags"
print str(parser.textBeforeTags("ab</p>") == "ab")
print str(parser.textBeforeTags("asdfasdfsa<as></as></asdf>") == "asdfasdfsa")
