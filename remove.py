from rembg import remove
from PIL import Image

""" input_path """
input_path = 'cd.jpg'
output_path = 'output.png'

output = remove(input)
input = Image.open(input_path)
 # the coment inserting by open-img
output.save(output_path)