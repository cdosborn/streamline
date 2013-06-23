import urllib2
from urllib2 import urlopen, URLError, HTTPError
import parse, adt, doc

invalidURL = True

while invalidURL:
    try:
        address = raw_input("Enter a valid URL: ")
        rawFile = urlopen(address)
        rawHTML = rawFile.read()
        original = open("original.html", "w")
        original.write(rawHTML);
        original.close()
        invalidURL = False

    except urllib2.URLError:
        print "The website linked to does not allow for web crawling. Please try a different website."

    except urllib2.HTTPError: # Unusual error, tends to happen when URL causes a non-GET HTTP request.
        print "The link causes a nonstandard HTTP request."

    except ValueError: # Invalid URL form
        print "You did not enter a valid URL. It should be in the form 'http://www.google.com'."

    except Exception: # Generic error, DOES NOT catch KeyboardInterrupt, SystemExit
        print "A generic error occurred."

def buildTree(html):
    return adt.Tree(parse.parse(html))

def buildHTML(tree, address, css):
    #body = tree.get("body").write()
    #title = tree.get("title").write()
    body = tree.write()
    newDoc = doc.htmlDoc(address, body, css)
    newDoc.build()

buildHTML(buildTree(rawHTML), address, "streamline.css")
