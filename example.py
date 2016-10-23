from utils import *
from filters import *

img = Image.open("images/test.jpg").convert("RGBA")
img2 = Image.open("images/test.png").convert("RGBA")


images = [img2]


trasformer = removeWhiteBackgroundTrasformer().then(addBackgroundAllPositionsTrasformer(img, 1))
trasformer = CompositeTrasformer(addBackgroundAllPositionsTrasformer(img, 200))


test(images, trasformer)

# add_images_graph("test", trasformer.trasform(images))
# plt.show()