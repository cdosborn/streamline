from urllib2 import urlopen
import re

address = raw_input("Enter a valid URL including the 'http://' section: ")
rawPage = urlopen(address)
rawHTML = rawPage.read()
htmlDict = {}

def parseHtmlTags(rawHTML, tagText, htmlDict):
	startTag = "<" + tagText + ">"
	endTag = "</" + tagText + ">"
	startIndex = rawHTML.find(startTag) + len(startTag)
	endIndex = rawHTML.find(endTag)
	while (startIndex > endIndex) and (startIndex != -1 or endIndex != -1):
		# print tagText, "(" + str(startIndex) + ", " + str(endIndex) + ")" 
		endIndex = rawHTML.find(endTag, endIndex + 1)
	# print tagText, "(" + str(startIndex) + ", " + str(endIndex) + ")"
	htmlDict[tagText] = rawHTML[startIndex:endIndex]

def makeHTML(htmlSource):
	out = open("scraped.html", "w")
	out.writelines("<html><head><title>")
	out.writelines(htmlSource["title"])
	out.writelines("</title></head><body>")
	out.writelines("<h1>" + htmlSource["title"] + "</h1>")
	out.writelines("<p>" + htmlSource["p"] + "</p>")
	out.writelines("</body></html>")
	out.close()

parseHtmlTags(rawHTML,"title", htmlDict)
parseHtmlTags(rawHTML,"p", htmlDict)

makeHTML(htmlDict)