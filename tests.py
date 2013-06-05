import parse
import adt

def test_closingTag():
    assert parse.closingTag("adsfasdf", "p") == -1
    assert parse.closingTag("adsfasdf", "p") == -1
    assert parse.closingTag("<p adsfasdf></p>", "p") == len("<p adsfasdf>")
    assert parse.closingTag("<p><p><p><p></p></p></p></p>", "p") == len("<p><p><p><p></p></p></p>")
    assert parse.closingTag("<durp>asdfsd</durp>asd</durp>ad", "durp") == len("<durp>asdfsd")
    assert parse._closHelper("</html>", "html") == 0

def test_textBeforeTags():
    assert parse.textBeforeTags("ab</p>") == "ab"
    assert parse.textBeforeTags("asdfasdfsa<as></as></asdf>") == "asdfasdfsa"
    assert parse.textBeforeTags("<html>") == ""

def test_parse():
    tree = adt.Tree(parse.parse("<p><p><p><p></p></p></p></p>"))
    assert tree.write() == "<p><p><p><p></p></p></p></p>"
