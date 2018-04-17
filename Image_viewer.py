from PIL import Image
from requests import Session as Download
import io

print("downloading image....")
fd = Download().get("http://media.salemwebnetwork.com/cms/BST/40297-inspirational.400w.tn.jpg")
print("converting...")
image_file = io.BytesIO(fd.raw.data)
print("opening image....")
im = Image.open(image_file)
print("have a nice day")
