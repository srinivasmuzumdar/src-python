# Python3 program to convert image to pdf under 300kb size.
# importing necessary libraries
import img2pdf
from PIL import Image
import os
import cv2
import numpy as np


# storing image path
img_path = ""
  
# storing pdf path
pdf_path = ""

def convert(img_path,pdf_path): 
	# opening image
	image = Image.open(img_path) 
  
	# converting into chunks using img2pdf
	pdf_bytes = img2pdf.convert(image.filename)
  
	# opening or creating pdf file
	file = open(pdf_path,"wb")
  
	# writing pdf files with chunks
	file.write(pdf_bytes)

	image.save("image_res.jpg")

	image.close()
  
	# closing pdf file
	file.close()
  
	# output
	print("Successfully made pdf file")

convert(img_path,pdf_path)
image_open = Image.open("image_res.jpg")
rotate_image = image_open.rotate(270)
rotate_image.save("image_res.jpg")

file_size = os.stat(pdf_path)

#Change the value below to change the limit for file size
while file_size.st_size >= 300000:
	path = pdf_path
	img = cv2.imread("image_res.jpg")

	[m,n,*o] = img.shape

	f = 2
	down_points = (m//f,n//f)

	img1 = cv2.resize(img,down_points,interpolation=cv2.INTER_LINEAR)

	cv2.imwrite("image_res.jpg",img1)
	r_image = "image_res.jpg"

	convert(img_path=r_image,pdf_path = path)
	
	file_size = os.stat(pdf_path)
	print(file_size.st_size)
 




