from filters import *


"""
 Execute filter on given value

"""
def execute(value, t):
	results = t.trasform(value)
	return results



def add_images_graph(title, images):

	fig = plt.figure()
	fig.canvas.set_window_title(title)

	plt.axis('off')

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


img = Image.open("test.jpg").convert('RGBA')
img2 = Image.open("tomato.jpg").convert('RGBA')
# background = Image.open("test.jpg").convert('RGBA')


images = [img, img2]


# trasformer = CompositeTrasformer(horizontalFlipTrasformer(), verticalFlipTrasformer())
# trasformer = removeWhiteBackgroundTrasformer().then(douleImageTrasformer())
trasformer = CompositeTrasformer(horizontalFlipTrasformer(),verticalFlipTrasformer()).then(douleImageTrasformer())
test(images, trasformer)
