import Image, sys

argv = sys.argv

img_name = argv[1].rsplit(".",1)[0]

img = Image.open(argv[1])
img = img.convert("RGBA")

pixdata = img.load()

html_top = """
<!DOCTYPE html>
<head>
<title>%s</title>
<style type='text/css'>
table tr {margin:0px; padding:0px; max-height:1px;}
table tr td {max-width:1px;}
</style>
</head>
<body>
<table cellspacing='0' cellpadding='0'>
""" % (img_name)

html_bottom = """
</table>
</body>
</html>
"""

f = open(img_name+".html", 'w')
f.write(html_top)
for y in xrange(img.size[1]):
    f.write("<tr>")
    colspan = 1
    previous_x = ()
    td_text = ""
    for x in xrange(img.size[0]):
        if previous_x == pixdata[x,y]:
            colspan += 1
        elif colspan > 1:
            td_text += "<td colspan='"+str(colspan)+"' style='background-color:rgba" + str(pixdata[x,y]) + ";'></td>"
            colspan = 1
        else:
            td_text += "<td style='background-color:rgba" + str(pixdata[x,y]) + ";'></td>"

        previous_x = pixdata[x,y]

    f.write(td_text+"</tr>")

f.write(html_bottom)
f.close()
