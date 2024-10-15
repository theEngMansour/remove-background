from rembg import remove
from PIL import Image

""" input_path """
input_path = 'cd.jpg'
output_path = 'output.png'

input = Image.open(input_path)
# the comment inserting by open-img
output = remove(input)
output.save(output_path)
