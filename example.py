from utils import *
from filters import *
import glob

path_png = "images/tomatoes/png"
path_jpg = "images/tomatoes/jpg"

path_bg = "images/backgrounds"
path_result = "images/results"

def load_all_images_in_folder(path):
	file_names = glob.glob(path + "/*.jpg")
	images = []
	for name in file_names:
		images.append(Image.open(name).convert("RGBA"))
	return images

def load_all_png_images_in_folder(path):
	file_names = glob.glob(path + "/*.png")
	images = []
	for name in file_names:
		images.append(Image.open(name).convert("RGBA"))
	return images

def convert_to_png(images, path):
	i = 1
	for im in images:
		im.save(path + "/" + str(i) + ".png")
		i = i + 1

def resize_all_images(images, x, y):
	resized = []
	for im in images:
		im.thumbnail((x,y), Image.ANTIALIAS)
		resized.append(im)
	return resized


# images = load_all_images_in_folder(path_jpg)
# convert_to_png(resize_all_images(images, 20, 20), path_png)

# bg1 = Image.open(path_bg + "/pic_001.jpg").convert("RGBA")
# bg2 = Image.open(path_bg + "/pic_002.jpg").convert("RGBA")

# backgrounds = [bg1, bg2]
backgrounds = load_all_images_in_folder(path_bg)

trasformer = removeWhiteBackgroundTrasformer().then(
	CompositeTrasformer(
		horizontalFlipTrasformer(), 
		verticalFlipTrasformer())).then(MultipleTrasformer([addBackgroundRandomPositionsTrasformer(background, 2) for background in backgrounds]))

# img = Image.open(path_png + "/1.png").convert("RGBA")
# img2 = Image.open(path_png + "/2.png").convert("RGBA")


# images = [img, img2]
images = load_all_png_images_in_folder(path_png)

# add_images_graph("test", images)
# plt.show()

convert_to_png(test(images, trasformer), path_result)


# trasformer = removeWhiteBackgroundTrasformer().then(addBackgroundAllPositionsTrasformer(img, 1))
# trasformer = addBackgroundRandomPositionsTrasformer(img, 10)


# test(images, trasformer)

# add_images_graph("test", trasformer.trasform(images))
# plt.show()