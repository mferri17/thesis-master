import os
import glob
import numpy as np
import matplotlib.pyplot as plt

images = glob.glob("*.jpg")

#plt.imshow(plt.imread(images[0]).astype('uint8'))
#plt.show()
#exit()

for path in images:
	img = plt.imread(path)
	img = img[70:-70, 25:-17]
	plt.imsave(path, img)