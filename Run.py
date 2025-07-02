import os
from ImagePassword import ImagePassword

input_image_path = input("Enter the path to the image: ")
input_filename = input("Enter the name of the image file: ")

if not os.path.exists(input_image_path):
    print("The specified image does not exist.")
else:
    image_password = ImagePassword(input_image_path)
    print("Image size:", image_password.get_image_size())
    encode = image_password.encode_image()
    print("Image loaded successfully.")
    print("Encoded image password successfully.")

    current_folder = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(current_folder, "Password")
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, input_filename + ".txt")
    with open(file_path, "w") as f:
        f.write(encode)
