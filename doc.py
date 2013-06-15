import uuid, os

# htmlDoc defines the properties/behaviors of a generated HTML document
class htmlDoc:

    # pre: URL address, HTML content, a filepath to a CSS file, a string title, a string name
    # post: an object with a unique ID, HTML meta info, HTML style info with a link to a CSS file
    #        an HTML header of the title, a link to the original, and HTML body content 
    def __init__(self, address=None, content=None, css=None, title=None, name=None): 
        if name:
            self.uid = name + ".html" # uid -- unique identifier
        else:
            self.uid = uuid.uuid4().hex + ".html" # generates unique string of 32 hexadecimal digits


        # Note: use ' in actual html, " for strings
        if os.path.exists("./streamlined/" + css):
            self.style = "<link href='http://fonts.googleapis.com/css?family=Oswald:400,700|Open+Sans' rel='stylesheet' type='text/css'>" + "\n" \
                    "<link rel='stylesheet' href='../" + css + "'>" + "\n"
        else:
            self.style = ""

        if title:
            self.meta   = "<title>" + title + "</title>" + "\n" + \
                     "<meta charset='utf-8'>" + "\n"
            self.header = "<h1>" + title + "</h1>" + "\n"
        else:
            self.meta   = "<meta charset='utf-8'>" + "\n"
            self.header = ""

        if content:
            self.content = content
        else:
            self.content = ""

        if address:
            self.link = "<br><h3><a href='" + address + "'>Link to the original article</a></h3><br>" + "\n"
        else:
            self.link = ""

    # pre: a UID, HTML style info, HTML meta info, HTML header info, HTML content, a HTML link
    # post: a valid HTML document containing the htmlDoc properties
    def build(self):
        if not os.path.exists("streamlined"):
            os.mkdir("streamlined")
        self.write = open("streamlined/" + self.uid, "w")


        self.write.writelines("<!DOCTYPE html>" + "\n" + \
                            "<html lang='en'>" + "\n" + \
                            "<head>" + "\n" + \
                            self.style + \
                            self.meta + \
                            "</head>" + "\n" + \
                            "<body>" + "\n" + \
                            "<div class='container'>" + "\n" + \
                            self.header + \
                            self.content + "\n" + \
                            self.link + \
                            "</div>" + "\n" + \
                            "</body>" + "\n" + \
                            "</html>" + "\n");
        self.write.close()


