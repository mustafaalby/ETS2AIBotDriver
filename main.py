import numpy as np
from PIL import ImageGrab
import cv2
import time
lastTime = time.time()
while (True):
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))
    print('while took: ', time.time()-lastTime)
    lastTime = time.time()
    cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
