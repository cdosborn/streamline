import parse
import adt

def test_closingTag():
    assert parse.closingTag("adsfasdf", "p") == -1
    assert parse.closingTag("adsfasdf", "p") == -1
    assert parse.closingTag("<p adsfasdf></p>", "p") == len("<p adsfasdf>")
    assert parse.closingTag("<p><p><p><p></p></p></p></p>", "p") == len("<p><p><p><p></p></p></p>")
    assert parse.closingTag("<durp>asdfsd</durp>asd</durp>ad", "durp") == len("<durp>asdfsd")
    assert parse._closHelper("</html>", "html") == 0
    assert parse.closingTag("<p><meta><meta></p>", "meta") == -1
    assert parse.closingTag("<p><head></head></p>", "head") == len("<p><head>")

def test_textBeforeTags():
    assert parse.textBeforeTags("ab</p>") == "ab"
    assert parse.textBeforeTags("asdfasdfsa<as></as></asdf>") == "asdfasdfsa"
    assert parse.textBeforeTags("<html>") == ""

def test_parse():
    tree = adt.Tree(parse.parse("<p><p><p><p></p></p></p></p>"))
    assert tree.write() == "<p><p><p><p></p></p></p></p>"
    tree2 = adt.Tree(parse.parse("<p><meta asd></p>"))
    assert tree2.write() == "<p><meta></p>"
    tree3 = adt.Tree(parse.parse("<html><link rel=stylesheet type=text/css href=/css/simple.css></html>"))
    assert tree3.write() == "<html><link></html>"
    tree4 = adt.Tree(parse.parse("<html><!--    <a href=https://bitbucket.org/cdosborn class=list><span class=entypo-bucket></span></a><a href=http://www.last.fm/user/cdosborn class=list><span class=entypo-lastfm></span></a><a href=mailto:iamnotajudas@gmail.com?subject=Howdy! class=list><span class=entypo-paper-plane></span></a> --></html>"))
    assert tree4.write() == "<html><--></html>"

test_parse()
