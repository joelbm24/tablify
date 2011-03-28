import tablify, sys

argv = sys.argv

img_name = argv[1].rsplit(".",1)[0]

tb = tablify.Tablify()
tb.init(50,50)

html_top = """
<!DOCTYPE html>
<head>
<title>TEST</title>
<style type='text/css'>
%s
</style>
</head>
<body>
""" % (tb.image(argv[1],20,20))

html_bottom = """
</body>
</html>
"""

f = open(img_name + '.html','w')
f.write(html_top)
f.write(tb.create_table())
f.write(html_bottom)
f.close()
