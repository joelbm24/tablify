import Image, sys

argv = sys.argv

img = Image.open(argv[1])
img = img.convert("RGB")

pixdata = img.load()

f = open(argv[2], 'w')
f.write("<table cellspacing='0'>")
for y in xrange(img.size[1]):
        f.write("<tr>")
        for x in xrange(img.size[0]):
            f.write("<td width='0.9' height='0.9' style='background-color:rgb" + str(pixdata[x,y]) + "'></td>")
        f.write("</tr>")
f.write("</table>")
