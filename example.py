from utils import *
from filters import *

img = Image.open("images/test.jpg")
img2 = Image.open("images/tomato.jpg")


images = [img, img2]


trasformer = CompositeTrasformer(horizontalFlipTrasformer(),verticalFlipTrasformer()).then(douleImageTrasformer())
test(images, trasformer) 
