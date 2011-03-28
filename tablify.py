import Image

class Tablify():
    def __init__(self):
        self.table = ""

    def init(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def create_table(self):
        self.table += "<table cellspacing='0'>"

        for y in xrange(self.size_y):
            self.table += "<tr>"
            td_text = ""

            for x in xrange(self.size_x):
                td_text += "<td id='b"+ str(x) + "-" + str(y) + "'>"
            self.table += td_text
            self.table += "</tr>"

        self.table += "</table>"
        return self.table

    def image(self, image_name, pos_x, pos_y):
        img_data = ""
        img = Image.open(image_name)
        img = img.convert("RGBA")
        pixdata = img.load()

        for y in xrange(self.size_y):
            td_text = ""
            for x in xrange(self.size_x):
                td_text += "#b"+str(x+pos_x)+"-"+str(y+pos_y) + " {background-color: " + "rgba" + str(pixdata[x,y]) +";}\n"


            img_data += td_text
        return img_data
