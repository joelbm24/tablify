import tablify, sys

argv = sys.argv

name = argv[1]

tb = tablify.Tablify()
tb.init(100,100)
tb.fill((255,0,0,255))
tb.rect(0,0,300,300)
tb.fill((1,1,1,255))
for i in xrange(10):
    tb.rect(i*10,i*10,10,10)

tb.blit(name)
