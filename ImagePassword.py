from PIL import Image
import hashlib

class ImagePassword:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size

    def get_image_size(self):
        return self.width, self.height
    
    def get_image(self):
        return self.image
    
    def encode_image(self) -> str:
        image_bytes = self.image.tobytes()

        width_bytes = int(self.width / 1000).to_bytes(4, 'big')
        height_bytes = int(self.height / 1000).to_bytes(4, 'big')

        all_bytes = image_bytes + width_bytes + height_bytes

        hashed = hashlib.sha256(all_bytes).hexdigest()
        return hashed
