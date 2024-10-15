from rembg import remove
from PIL import Image

""" input_path """
output_path = 'output.png'
input_path = 'cd.jpg'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)