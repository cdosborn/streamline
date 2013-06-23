import re
import adt

# post: returns the index of the closing tag which matches the first found
#       occurence of the opening tag
def closingTag(html, tag, level=0, _index=0):
    #html has a valid beginning tag
    start = html.find("<" + tag)
    if start == -1:
        return -1
    #get index after tag and its attributes
    indexAfterOpenTag = start + html[start:].find(">") + 1
    return _closHelper(html[indexAfterOpenTag:], tag, 0, indexAfterOpenTag)

# pre:  the initial tag to be matched is not part of the string
# post: recurses with nested tags and returns correct index after returning to the original level
def _closHelper(html, tag, level=0, _index=0):
    opening = "<" + tag + ">"
    closing = "</" + tag + ">"
    openTag = html.find(opening)
    closTag = html.find(closing) 
    nextTag = min(openTag, closTag)
    if nextTag == -1:
        nextTag = max(openTag, closTag)
    if nextTag == -1 or html == "":
        return -1;
    elif level == 0 and nextTag == closTag:
        return  _index + closTag
    elif nextTag == openTag:
        return _closHelper(html[openTag + len(opening):], tag, level + 1, _index + openTag + len(opening))
    else:
        return _closHelper(html[closTag + len(closing):], tag, level - 1, _index + closTag + len(closing))

# post: returns the text before a "<" (tag) or everything if no tag is found
def textBeforeTags(html):
    end = html.find("<")
    if end == -1:
        return html
    return html[:end]

def parse(html):
    # this is the root node of an html doc, a comment, doctype, html could be valid children
    node = adt.Node("Super")
    while html is not "":
        pattern = re.compile("<(!--)[^\1]*?-->|<[!/]?([\w-]+)[^\2]*?>")
        # recurse on the html of the next tag
        match = pattern.match(html)
        # comment tags return None for .group(2) and the appropriate tag for .group(1)

        # This code is directly copied from _parse needs to be refactored!
        if match.group(1): #matches a comment tag
            tag = match.group(1)
        else:              #matches every other tag
            tag = match.group(2)
        
        if closingTag(html, tag) is -1:
            node.addNoClosingChild(tag)
            html = html[len(match.group()):]
        else:
            next_html = html[:closingTag(html, tag) + len("</" + tag + ">")]
            node.addChild(_parse(next_html))
            html = html[len(next_html):]
        whitespace = textBeforeTags(html)
        html = html[len(whitespace):]
    return node

# post: returns a node for an html tag where its subtrees are its directly nested tags
def _parse(html):
    # pattern is a regex for matching any tag
    pattern = re.compile("<(!--)[^\1]*?-->|<[!/]?([\w-]+)[^\2]*?>")

    # match is the object result of matching the regex 
    # to the beginning of the html
    match = pattern.match(html)
    if match:
        if match.group(1): #matches a comment tag
            tag = match.group(1)
        else:              #matches every other tag
            tag = match.group(2)

        node = adt.Node(tag)
        # trims off beginning and closing tag of html
        body = html[match.end(): closingTag(html,tag)]

        # pulls out any text before a tag, recurses on any tag pair
        # while there are more children to process      
        while len(body) > 0:
            # pull out text before
            text = textBeforeTags(body)
            node.addTextChild(text)
            body = body[len(text):]

            # recurse on the html of the next tag
            nextMatch = pattern.match(body)
            # comment tags return None for .group(2) and the appropriate tag for .group(1)
            if nextMatch:
                if nextMatch.group(2): # non-comment tag
                    nextTag = nextMatch.group(2)
                else:                  #comment tag
                    nextTag = nextMatch.group(1)
                
                if closingTag(body, nextTag) is -1:
                    node.addNoClosingChild(nextTag)
                    body = body[len(nextMatch.group()):]
                elif nextTag is "script" or nextTag is "style":
                    node.addChild(adt.Node(nextTag)) 
                    body = body[closingTag(body, nextTag) + len("</" + nextTag + ">"):]
                else:
                    nextHtml = body[:closingTag(body, nextTag) + len("</" + str(nextTag) + ">")]
                    node.addChild(_parse(nextHtml))
                    body = body[len(nextHtml):]
        return node
    else:
        return None
