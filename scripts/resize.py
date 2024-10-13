from os import path, getcwd
from PIL import Image
from sys import exit

class Colors:
    SUCCESS = '\033[92m'
    ERROR = '\033[91m'
    RESET = '\033[0m'

resize = (230, 255)

input_file = "file.ext"
output_file = "output.png"

input_path = path.join(getcwd(), input_file)
output_path = path.join(getcwd(), output_file)

if not path.exists(input_path):
    print(f"[{Colors.ERROR}ERROR{Colors.RESET}] No such file: '{input_path}\'")
    exit(1)

if not path.isfile(input_file):
    print(f"[{Colors.ERROR}ERROR{Colors.RESET}] Expected a file, but got a directory: '{input_path}\'")
    exit(1)

try:
    old_img = Image.open(input_path)
    
    new_image = old_img.resize(resize)
    new_image.save(output_path, format="PNG", compress_level=0)

    print(f"[{Colors.SUCCESS}SUCCESS{Colors.RESET}] \"{output_file}\" saved with success.")
    exit(0)
except Exception as err:
    print(f"[{Colors.ERROR}ERROR{Colors.RESET}] {err}")
    exit(1)