from matplotlib import pyplot as plt
import math



"""
 Execute filter on given value

"""
def execute(value, t):
	results = t.trasform(value)
	return results



def add_images_graph(title, images):

	fig = plt.figure()
	fig.canvas.set_window_title(title)

	image_number = len(images)

	x = int(math.sqrt(image_number))
	y = x

	while x*y < image_number:
		y = y + 1

	for i in range(image_number):
		graph = fig.add_subplot(x,y,i+1)
		graph.imshow(images[i])




"""
 Show input images and output images of trasformer

"""
def test(inputs, trasformer):
	processed_img = execute(inputs, trasformer)
	add_images_graph("Inputs", inputs)
	add_images_graph("Processed", processed_img)
	plt.show()
	return processed_img



def load_all_images_in_folder(path):
	file_names = glob.glob(path + "/*.jpg")
	images = []
	for name in file_names:
		images.append(Image.open(name).convert("RGBA"))
	return images



def load_n_images_in_folder(path, n):
	i = 0
	file_names = glob.glob(path + "/*.jpg")
	images = []
	while i < n:
		images.append(Image.open(file_names[i]).convert("RGBA"))
		i = i + 1
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



def convert_to_jpg(images, path):
	i = 1
	for im in images:
		im.save(path + "/" + str(i) + ".jpg")
		i = i + 1


"""
 Mantain images ratio

"""
def resize_all_images(images, x, y):
	resized = []
	for im in images:
		im.thumbnail((x,y), Image.ANTIALIAS)
		resized.append(im)
	return resized


"""
 Don't mantain images ratio
 
"""
def resize_exactly_all_images(images, x, y):
	resized = []
	for im in images:
		im = im.resize((x,y), Image.ANTIALIAS)
		resized.append(im)
	return resized



"""
 Prepare Images to be fed into Keras Model

 WORK IN PROGRESS

"""
def adapt_shape(images):
	result = []
	for im in images:
		im = (np.array(im))

		r = im[:,:,0]
		g = im[:,:,1]
		b = im[:,:,2]

		result.append([r,g,b])
	return np.array(result)



