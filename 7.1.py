from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
im = Image.open('d:\\bj.jpg')
im.thumbnail((128,128))
im.save('d:\\bjTN.jpg')
im = Image.open('d:\\bj.jpg')
r,g,b = im.split()
om = Image.merge("RGB",(b,g,r))
om.save('d:\\bjBGR.jpg')
newg = g.point(lambda i:i*0.9)
newb = g.point(lambda i:i<100)
om = Image.merge(im.mode,(r,newg,newb))
om.save('d:\\bjME.jpg')
om=im.filter(ImageFilter.CONTOUR)
om.save('d:\\bjCT.jpg')
om=ImageEnhance.Contrast(im)
om.enhance(20).save('d:\\bjEC.jpg')
