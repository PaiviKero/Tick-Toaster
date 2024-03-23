import cv2
from PIL import Image, ImageTk
import queue

from defs import *

class WebCam:
    
    def __init__(self, parent, campanel):
        self.parent = parent
        self.campanel = campanel
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW )
        bright = 128    # How bright to set the camera image
        focus = 0       # Focal value for the camera.
        self.cam.set(cv2.CAP_PROP_BRIGHTNESS, (bright)) 
        self.cam.set(cv2.CAP_PROP_FOCUS, (focus))  
        self.queue = queue.Queue()
        self.stream()

    def stream(self):
        ret, img = self.cam.read()
        if(ret):
            #cv2.imshow("Stream Video",img)
            self.update_image(img)
        self.campanel.after(25, self.stream)

    def update_image(self, img):
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image=Image.fromarray(image)
        image = image.resize(self.calculate_background_image_size(self.parent.winfo_height(), image.size))
        image = ImageTk.PhotoImage(image=image)
        self.campanel.configure(image=image) 
        self.image = image

    def calculate_background_image_size(self, height, original_size):
        new_height = height*CAMERA_IMAGE_SCALING_PERCENTAGE
        original_width, original_height = original_size
        new_width = original_width*(new_height/original_height)
        return (int(new_width), int(new_height))

    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()