import cv2
from matplotlib import pyplot as plt
import numpy as np

img1 = cv2.imread('imagen.extencion',2)
img2 = np.zeros(img1.shape,dtype=np.int32)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        if(img1[i][j] <= 127):
            img2[i][j] = 0
        if(img1[i][j] > 127):
            img2[i][j] = 255

ret,thresh1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)

plt.subplot(1,3,1)
plt.imshow(img1, 'gray')
plt.title('Popocatépetl')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(img2, 'gray')
plt.title('MANUAL')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(thresh1, 'gray')
plt.title('THRESHOLD')
plt.axis('off')

plt.show()
