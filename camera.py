import time
from picamera import PiCamera
fr=100
camera=PiCamera()
camera.start_preview(alpha=50)
camera.rotation=180
camera.framerate=fr
time.sleep(30)
camera.stop_preview()
