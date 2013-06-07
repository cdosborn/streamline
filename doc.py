import uuid, os

class htmlDoc:
    def __init__(self, address, body, css, title=None, name=None): # title can be plaintext, body must be valid HTML, name optional
        if name:
            self.uid = name + ".html" # uid -- unique identifier
        else:
            self.uid = uuid.uuid4().hex + ".html" # generates unique string of 32 hexadecimal digits

        if not os.path.exists("streamlined"):
            os.mkdir("streamlined")
        self.doc = open("streamlined/" + self.uid, "w")

        if css:
            self.doc.writelines(
                """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <link href='http://fonts.googleapis.com/css?family=Oswald:400,700|Open+Sans' rel='stylesheet' type='text/css'>
                <link rel='stylesheet' href='../streamline.css'>
                <meta charset="utf-8">
                """)
        else:
            self.doc.writelines(
                """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="utf-8">
                """)

        if title:
            titletag = "<title>" + title + "</title>"
            self.doc.writelines(titletag)

        self.doc.writelines(
            """
            </head>
            <body>
            <div class='container'>
            """)
        if title:
            self.doc.writelines("<h1>" + title + "</h1>")
        self.doc.writelines("<br><h3><a href='" + address + "'>Link to the original article</a></h3><br>")
        if body:
            self.doc.writelines(body)
            
        self.doc.writelines(
            """
            </div>
            </body>
            </html>
            """)
        self.doc.close()

# example run
# doc = htmlDoc("http://www.google.com", "<p>Lorem ipsum dolor sit amet.</p>", True)
