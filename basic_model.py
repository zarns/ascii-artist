import os
import sys
import numpy as np
from PIL import Image

def img_resizer(img, new_width, ratio_multiplier):
    """Resize the image based on the new width
    """
    
    w, h = img.size
    
    assert w >= new_width, "New width must be smaller than old width"
    
    ratio = ratio_multiplier * h / w
    
    new_height = int(ratio * new_width)
    
    resized_img = img.resize((new_width, new_height))
    
    return resized_img

def img_to_ascii(img, ASCII, output_path):
    """Convert image to ASCII characters
    """
    
    ascii_img = []
    img_arr = np.array(img)
    
    for ind, i in enumerate(img_arr):
        ascii_img.append('')
        for j in i:
            indx = (j * (len(ASCII)-1)) // 255
            ascii_char = ASCII[indx]
            ascii_img[ind] += ascii_char
        ascii_img[ind] += '\n'
    
    output_path = os.path.join(output_path)

    with open(output_path, 'w') as f:
        f.writelines(ascii_img)
    
if __name__ == '__main__':
    args = sys.argv
    assert len(args) >= 2, "Must include filepath"
    img_path_argument = args[1]
    if len(args) > 2:
        img_width = args[2]
    else:
        img_width = 100

    if len(args) > 3:
        ratio_multiplier = args[3]
    else:
        ratio_multiplier = 1
        
    # Play around with alternative ascii values. Simply order them from darkest to lightest:
    ASCII = "@%#*+=-:. "
    # ASCII = "$@B%8W#*hkbdpqwmZOQLCJXzxrjft1+<>i!l:. "

    try:
        img_path = os.path.join("images/", img_path_argument)
        img = Image.open(img_path).convert('L')
        
        if img_width:
            resized_img = img_resizer(img, new_width=img_width, ratio_multiplier=ratio_multiplier)
        else:
            resized_img = img_resizer(img, new_width=100)
        
        current_path = os.path.abspath(os.curdir)
        input_without_suffix = os.path.splitext(img_path_argument)[0]
        output_path = os.path.join(current_path, "basic_output/", input_without_suffix) + ".txt"
        img_to_ascii(resized_img, ASCII, output_path)
            
    except Exception as error:
        print("Error: {error}".format(error=error))