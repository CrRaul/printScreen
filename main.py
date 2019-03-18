import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'top': 250, 'left': 250, 'width': 450, 'height': 550}

sct = mss()

i = 0
while 1:
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    cv2.imshow('test', np.array(img))
    cv2.imwrite('im'+str(i)+".jpg", np.array(img))
    i+=1
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break