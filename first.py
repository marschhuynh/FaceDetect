from PIL import Image,ImageFilter


pic = Image.open('example.jpg')

pic.show()

pic_sharp = pic.filter(ImageFilter.SHARPEN)

pic_sharp.save('example_sharp.jpg','JPEG')

pic_sharp.show()


