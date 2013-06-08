import re
import adt

# Parser and helper methods
# ------------------------

# assumes that html includes the first instance of the opening tag
def closingTag(html, tag, level=0, _index=0):
    #html has a valid beginning tag
    start = html.find("<" + tag)
    if start == -1:
        return -1
    #get index after tag and its attributes
    indexAfterOpenTag = html[start:].find(">") + 1
    return _closHelper(html[indexAfterOpenTag:], tag, 0, indexAfterOpenTag)

# handles the bulk of the recursion the above method just
# prepares the html for recursion
def _closHelper(html, tag, level=0, _index=0):
    opening = "<" + tag + ">"
    closing = "</" + tag + ">"
    openTag = html.find(opening)
    closTag = html.find(closing) 
    nextTag = min(openTag, closTag)
    if nextTag == -1:
        nextTag = max(openTag, closTag)
    # TESTS
    # print "searching: " + html + " at level,index: " + str(level) + ", " + str(_index)
    if nextTag == -1 or html == "":
        return -1;
    elif level == 0 and nextTag == closTag:
    #   print "found at: " + str(_index + closTag)
        return  _index + closTag
    elif nextTag == openTag:
        return _closHelper(html[openTag + len(opening):], tag, level + 1, _index + openTag + len(opening))
    else:
        return _closHelper(html[closTag + len(closing):], tag, level - 1, _index + closTag + len(closing))

# returns the text before a "<" (tag) or everything if no tag is found
def textBeforeTags(html):
    end = html.find("<")
    if end == -1:
        end = len(html)
    text = html[:end]
    return text;

def parse(html):
    # pattern is a regex for matching any tag
    pattern = re.compile("<[!|/]?([\w|-]+)[^>]*>")
    # match is the object result of matching the regex to the html 
    # it only matches text found at the beginning of a string
    match = pattern.match(html)
    if match:
        tag = match.group(1)
        node = adt.Node(tag)
        # trims off beginning and closing tag of html
        body = html[match.end():len(html) - len("</" + tag + ">")]

        # pulls out any text before a tag, recurses on any tag pair
        # while there are more children to process      
        while len(body) > 0:
            # print "body: " + body
            # pull out text before
            text = textBeforeTags(body)
            # print "text: " + text
            node.addTextChild(text)
            body = body[len(text):]
            
            # recurse on the html of the next tag
            nextMatch = pattern.match(body)
            if nextMatch:
                nextTag = nextMatch.group(1)
                # print "--> deeper with: " + body[:closingTag(body, nextTag) + len("</" + nextTag + ">")]
                if closingTag(body, nextTag) == -1:
                    node.addNoClosingChild(nextTag)
                    body = body[len(nextMatch.group()):]
                else:
                    nextHtml = body[:closingTag(body, nextTag) + len("</" + nextTag + ">")]
                    node.addChild(parse(nextHtml))
                    body = body[len(nextHtml):]
                # print "<-- exit, body rem: " + body[len(nextHtml):]
        return node
    else:
        return None
