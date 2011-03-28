import tablify, sys

argv = sys.argv

name = argv[1]

tb = tablify.Tablify()
tb.init(300,300)
tb.fill((255,0,0,255))
tb.rect(0,0,300,300)
tb.image('apple1.gif',125,125)


html_top = """
<!DOCTYPE html>
<head>
<title>TEST</title>
<style type='text/css'>
%s
</style>
</head>
<body>
    """ % (tb.style())

html_bottom = """
</body>
</html>
"""

f = open(name + '.html','w')
f.write(html_top)
f.write(tb.create_table())
f.write(html_bottom)
f.close()
