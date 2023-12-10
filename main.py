import camera
from time import sleep

print("Start connection")


camera.Camera()
camera.Camera.preview()
camera.Camera.capture_image(file_path='1.jpg')
sleep(10)
camera.Camera.stop_preview()
