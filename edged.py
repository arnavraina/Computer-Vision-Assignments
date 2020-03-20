from PIL import ImageFilter
from PIL import Image
im = Image.open('night_image.jpeg')
im = im.filter(ImageFilter.FIND_EDGES)
im.show()
