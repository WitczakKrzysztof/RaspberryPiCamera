import picamera
import time

# Create a camera object
camera = picamera.PiCamera()

# Set camera resolution (optional)
camera.resolution = (640, 480)

# Start the preview
camera.start_preview()

# Give the camera some warm-up time
time.sleep(2)

# Capture the camera view
camera.capture('camera_view.jpg')

# Stop the preview
camera.stop_preview()