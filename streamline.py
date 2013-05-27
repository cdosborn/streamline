from urllib2 import urlopen

'''Sends a request for the HTML document at "address", 
stores the file in rawPage, and then reads it into a 
raw HTML document in rawHTML.'''

try:
	address = raw_input("Enter a valid URL: ")
	rawPage = urlopen(address)
	rawHTML = rawPage.read()
	htmlDict = {}
except:
	print "Request could not be completed, the site probably doesn't allow for scraping."

'''Parses a raw HTML string (rawHTML) for all elements 
matching the HTML tag (tagText) and 
stores all instances of that tag in a dictionary.'''

def parseHtmlTags(rawHTML, tagText, htmlDict):
	startTag = "<" + tagText + ">"
	endTag = "</" + tagText + ">"

	startIndex = 0
	endIndex = 0

	dictItemNum = 0
	htmlDict[tagText] = ""
	itemIndex = tagText + str(dictItemNum)
	itemDict = {}

	while startIndex != -1 and endIndex != -1:
		startIndex = rawHTML.find(startTag, startIndex + 1)
		endIndex = rawHTML.find(endTag, endIndex + 1)
		if startIndex == -1 and endIndex == -1:
			break
		if startIndex > endIndex:
			while startIndex > endIndex:
				endIndex = rawHTML.find(endTag, endIndex + 1)
		snippet = rawHTML[startIndex + len(startTag):endIndex]
		if isArticleText(snippet):
			itemDict[itemIndex] = snippet

		dictItemNum += 1
		itemIndex = tagText + str(dictItemNum)

	htmlDict[tagText] = itemDict

def isArticleText(inputHtml):
	forbidden = ["<script", "<form", "<input", "DOCTYPE", "<span"]
	for item in forbidden:
		if inputHtml.find(item) != -1:
			return False
	return True

'''Creates a barebones HTML document and adds the 
extracted elements contained in htmlDict with the 
necessary HTML formatting in between.'''

def makeHTML(htmlDict, address):
	htmlFile = open("streamlined.html", "w")
	htmlFile.writelines(
"""
<!DOCTYPE html>
<html lang="en">
<head>
<link href='http://fonts.googleapis.com/css?family=Oswald:400,700|Open+Sans' rel='stylesheet' type='text/css'>
<link href='streamline.css' rel='stylesheet'>
<meta charset="utf-8">
"""
		)
	htmlFile.writelines("<title>" + htmlDict["title"]["title0"] + "</title>")

	htmlFile.writelines(
"""
</head>
<body>
"""
		)
	htmlFile.writelines("<h1>" + htmlDict["title"]["title0"] + "</h1>")
	htmlFile.writelines("<br><h3><a href='" + address + "'>Link to the original article</a></h3><br>")

	numPItems = len(htmlDict["p"])
	for item in range(1, numPItems):
		keystr = "p" + str(item)
		htmlFile.writelines("<br><p>" + htmlDict["p"][keystr] + "</p>")

	htmlFile.writelines(
"""
</body>
</html>
"""
		)
	htmlFile.close()

# def makeCSS(color, fontstyle):


parseHtmlTags(rawHTML,"title", htmlDict)
parseHtmlTags(rawHTML,"p", htmlDict)
makeHTML(htmlDict, address)
