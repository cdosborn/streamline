import parse, adt, doc, re

def test_regex():
    pattern = re.compile("<(!--)[^\1]*?-->|<[!/]?([\w-]+)[^\1]*?>")
    match = pattern.match("<p>asdf</p>")
    assert match.group(2) == "p"


def test_parse_closingTag():
    # private excludes occurence of first tag
    assert parse._closHelper("</html>", "html") == 0
    # no tag is found
    assert parse.closingTag("adsfasdf", "p") == -1
    # tag has attributes
    assert parse.closingTag("<p adsfasdf></p>", "p") == len("<p adsfasdf>")
    # tag is heavily nested
    assert parse.closingTag("<p><p><p><p></p></p></p></p>", "p") == len("<p><p><p><p></p></p></p>")
    # multiple end tags are present  
    assert parse.closingTag("<durp>asdfsd</durp>asd</durp>ad", "durp") == len("<durp>asdfsd")
    # opening and closing tag are not first
    assert parse.closingTag("<p><meta></meta></p>", "meta") == len("<p><meta>")
    # self closing tags return -1
    assert parse.closingTag("<p><head><head></p>", "head") == -1
    # style including brackets is overcome
    assert parse.closingTag("<style> a > p { <!-- <tag>a</tag>}</style>", "style") == len("<style> a > p { <!-- <tag>a</tag>}") 

def test_parse_textBeforeTags():
    # text followed by tag
    assert parse.textBeforeTags("ab</p>") == "ab"
    # tag w/o text
    assert parse.textBeforeTags("<html>") == ""
    # text w/o tag
    assert parse.textBeforeTags("asdf") == "asdf"

def test_parse_parse():
    tree = adt.Tree(parse.parse("<p><p><p><p></p></p></p></p>"))
    assert tree.write() == "<document><p><p><p><p></p></p></p></p></document>"
    tree2 = adt.Tree(parse.parse("<p><meta asd></p>"))
    assert tree2.write() == "<document><p><meta></p></document>"
    tree3 = adt.Tree(parse.parse("<html><link rel=stylesheet type=text/css href=/css/simple.css></html>"))
    assert tree3.write() == "<document><html><link></html></document>"
    # test comment parsing
    tree4 = adt.Tree(parse.parse("<html><!--   <a></a> --></html>"))
    assert tree4.write() == "<document><html><!--></html></document>"

def test_tree_get():
    # basic nesting
    tree = adt.Tree(parse.parse("<a><b><c></c></b></a>"))
    assert tree.get("c").write() == "<c></c>"
    tree = adt.Tree(parse.parse("<p><meta></p>"))
    # self-closing node
    assert tree.write() == "<document><p><meta></p></document>"
    assert tree.get("p").write() == "<p><meta></p>"

#def test_doc():
#    testDoc = doc.htmlDoc("http://www.google.com", "<p>Lorem ipsum dolor sit amet.</p>", None, "My Test File")
#    
#    # test uid field
#    assert testDoc.uid == 37
#
#    # test link field
#    assert testDoc.link.find("http://www.google.com") != -1
#
#    # test meta field
#    assert testDoc.meta.find("My Test File") != -1
