import cv2
import sys
def resize_aspect(path,percent): 
	img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
	print('Original Dimensions : ',img.shape)
	scale_percent = int(percent) # percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	print('Resized Dimensions : ',resized.shape)
	cv2.imshow("Resized image", resized)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
def resize_noaspect(path,w,h): 
	img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
	print('Original Dimensions : ',img.shape)
	
	dim = (int(w), int(h))
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	print('Resized Dimensions : ',resized.shape)
	cv2.imshow("Resized image", resized)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
def grayscale(path):
	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#cv2.imshow('Original image',image)
	cv2.imshow('Gray image', gray)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
def convert(outpath, inpath, jpg_quality=None, png_compression=None):
 
#jpg_quality: for jpeg only. 0 - 100 (higher means better). Default is 95.
#png_compression: For png only. 0 - 9 (higher means a smaller size and longer compression time).
#Default is 3.
	image = cv2.imread(inpath)
	if jpg_quality:
		cv2.imwrite(outpath, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
	elif png_compression:
		cv2.imwrite(outpath, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
	else:
		cv2.imwrite(outpath, image)
	new_img=cv2.imread(outpath)
	cv2.imshow('Converted image',new_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
if __name__ == '__main__':
	if(len(sys.argv)==2):
		print('Path is '+sys.argv[1])
		grayscale(sys.argv[1])
	if(len(sys.argv)==3):
		print('Path is '+sys.argv[1]+' and percent is '+sys.argv[2])
		resize_aspect(sys.argv[1],sys.argv[2])
	if(len(sys.argv)==4):
		print('Path is '+sys.argv[1]+' and percent is '+sys.argv[2])
		resize_noaspect(sys.argv[1],sys.argv[2],sys.argv[3])
	if(len(sys.argv)==1):
		print("\r\nConversion\r\n")
		inpath=input('Choose input path : ')
		outpath=input('Choose output path : ')
		choice=input('Choose conversion format (jpg,png) : ')
		ratio=int(input('Choose optimisation ratio -- for jpeg (0 - 100), For png (0 - 9) : '))
		if(choice=='jpg'):
			convert(outpath,inpath,ratio,None)
		elif(choice=='png'):
			convert(outpath,inpath,None,ratio)
		print('Conversion Success')