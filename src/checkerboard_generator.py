import math,cairo
import numpy as np


# height of the surface, in points (1 point = 1/72.0 inch)
#


#pdf_width, pdf_height = 8.5, 11.0 #inch

rectangle_width_size_mm =  30 #mm  

rectangle_width_size = rectangle_width_size_mm*0.03937007874#inch

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)

#                         border space
rows = math.floor((pdf_width) / rectangle_width_size)
# make grid cols and rows is odd / even or even / odd

yv = np.linspace(0, rows-1, rows)
# xv, yv = np.meshgrid(x,y, sparse=False, indexing='ij')
# yv = np.linspace(0,rows,1)
# print(xv)
print(yv)

# vertical_space = (pdf_height - checkerboard_size*rows) / 2
# horizontal_space = (pdf_width - checkerboard_size*cols) /2

# print(xv.shape[0])
ctx = cairo.Context (surface)
ctx.set_source_rgb(0,0,0)
for i in range(yv.shape[0]):
	if( i%2 == 1 ):
		ctx.rectangle(0,yv[i]*rectangle_width_size*72,pdf_width*72,rectangle_width_size*72)
		ctx.fill()
surface.write_to_png('filename')
