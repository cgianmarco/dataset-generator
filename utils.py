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
	# add_images_graph("Inputs", inputs)
	# add_images_graph("Processed", processed_img)
	# plt.show()
	return processed_img



