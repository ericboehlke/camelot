import io
import time
import picamera
from PIL import Image
import apriltag
at_detector = apriltag.Detector()
# Create the in-memory stream
while True:
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream).convert('LA')
    tags = at_detector.detect(image)

      # If we see any...
    if len(tags) != 0:
        # We can just consider the first tag we see
        tag = tags[0]

        # Print out tag ID. We will use distinct tag IDs for the goals and dispensers
        print("Tag ID: {}".format(tag.tag_id))
