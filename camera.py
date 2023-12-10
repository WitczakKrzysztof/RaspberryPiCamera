import picamera


class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera()

    def capture_image(self, file_path):
        self.camera.capture(file_path)

    def preview(self):
        self.camera.start_preview()

    def stop_preview(self):
        self.camera.stop_preview()

    def close(self):
        self.camera.close()

