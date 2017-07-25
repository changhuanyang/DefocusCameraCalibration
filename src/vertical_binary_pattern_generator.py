import math,cairo
import numpy as np


# height of the surface, in points (1 point = 1/72.0 inch)
#




# pdf_width, pdf_height = 20.0, 20.0 #inch

# checkerboard_size_mm =  30 #mm  

# checkerboard_size = checkerboard_size_mm*0.03937007874#inch

# surface = cairo.PDFSurface ("checkerboard.pdf", pdf_width*72.0, pdf_height*72.0)

WIDTH, HEIGHT = 1920, 1080

checkerboard_size = 100

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)
ctx.scale (WIDTH, HEIGHT) # Normalizing the canvas
# background color
ctx.set_source_rgb(1,1,1)
ctx.rectangle(0,0,WIDTH,HEIGHT)
ctx.fill()

vertical_space = 50
horizontal_space = 50

rows = math.floor((HEIGHT-vertical_space*2) / checkerboard_size)
# make grid cols and rows is odd / even or even / odd
cols = math.floor((WIDTH-horizontal_space*2) / checkerboard_size) - (rows%2)

x = np.linspace(0, cols-1, cols)
y = np.linspace(0, rows-1, rows)
xv, yv = np.meshgrid(x,y, sparse=False, indexing='ij')

print(xv)
print(yv)



print(xv.shape[0])
ctx = cairo.Context (surface)
ctx.set_source_rgb(0,0,0)
for i in range(xv.shape[0]):
	if( i%2 == 1):
		for j in range(0,xv.shape[1],1):
			if(j%2 ==1):
				ctx.rectangle((horizontal_space+xv[i][j]*checkerboard_size),(vertical_space),checkerboard_size,HEIGHT-2*vertical_space)
				ctx.fill()
	# else:

		# for j in range(1,xv.shape[1],2):
		# 	ctx.rectangle((horizontal_space+xv[i][j]*checkerboard_size),(vertical_space+yv[i][j]*checkerboard_size),checkerboard_size,checkerboard_size)
		# 	ctx.fill()

surface.write_to_png ("pattern6.png") # Output to PNG