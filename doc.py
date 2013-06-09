import uuid, os

class htmlDoc:
    def __init__(self, address=None, content=None, css=None, title=None, name=None): 
        if name:
            self.uid = name + ".html" # uid -- unique identifier
        else:
            self.uid = uuid.uuid4().hex + ".html" # generates unique string of 32 hexadecimal digits

        if not os.path.exists("streamlined"):
            os.mkdir("streamlined")
        self.doc = open("streamlined/" + self.uid, "w")

        # Note: use ' in actual html, " for strings
        if os.path.exists("./streamlined/" + css):
            style = "<link href='http://fonts.googleapis.com/css?family=Oswald:400,700|Open+Sans' rel='stylesheet' type='text/css'>" + "\n" \
                    "<link rel='stylesheet' href='../" + css + "'>" + "\n"
        else:
            style = ""

        if title:
            meta   = "<title>" + title + "</title>" + "\n" + \
                     "<meta charset='utf-8'>" + "\n"
            header = "<h1>" + title + "</h1>" + "\n"
        else:
            meta   = "<meta charset='utf-8'>" + "\n"
            header = ""

        if not content:
            content = ""

        if address:
            link = "<br><h3><a href='" + address + "'>Link to the original article</a></h3><br>" + "\n"
        else:
            link = ""

        self.doc.writelines("<!DOCTYPE html>" + "\n" + \
                            "<html lang='en'>" + "\n" + \
                            "<head>" + "\n" + \
                            style + \
                            meta + \
                            "</head>" + "\n" + \
                            "<body>" + "\n" + \
                            "<div class='container'>" + "\n" + \
                            header + \
                            content + "\n" + \
                            link + \
                            "</div>" + "\n" + \
                            "</body>" + "\n" + \
                            "</html>" + "\n");
        self.doc.close()

# example run
#doc = htmlDoc("http://www.google.com", "<p>Lorem ipsum dolor sit amet.</p>", "streamline.css")
