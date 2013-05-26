from urllib2 import urlopen

'''Sends a request for the HTML document at "address", 
stores the file in rawPage, and then reads it into a 
raw HTML document in rawHTML.'''

address = raw_input("Enter a valid URL:")
rawPage = urlopen(address)
rawHTML = rawPage.read()
htmlDict = {}

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
		if startIndex > endIndex:
			while startIndex > endIndex:
				endIndex = rawHTML.find(endTag, endIndex + 1)

		itemDict[itemIndex] = rawHTML[startIndex + len(startTag):endIndex]

		dictItemNum += 1
		itemIndex = tagText + str(dictItemNum)

	htmlDict[tagText] = itemDict

'''Creates a barebones HTML document and adds the 
extracted elements contained in htmlDict with the 
necessary HTML formatting in between.'''
def makeHTML(htmlDict):
	htmlFile = open("streamlined.html", "w")
	htmlFile.writelines(
		"""
		<!DOCTYPE html>
		<html lang="en">
		<head>
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

	numPItems = len(htmlDict["p"])
	for item in range(1, numPItems):
		keystr = "p" + str(item)
		htmlFile.writelines("<p>" + htmlDict["p"][keystr] + "</p>")

	htmlFile.writelines(
		"""
		</body>
		</html>
		"""
		)

	htmlFile.close()

parseHtmlTags(rawHTML,"title", htmlDict)
parseHtmlTags(rawHTML,"p", htmlDict)
makeHTML(htmlDict)
