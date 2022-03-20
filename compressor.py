from PIL import Image
import sys
import numpy as np

image_file = sys.argv[1]
compression = int(sys.argv[2])

def compress_channel(channel):
    u, s, vh = np.linalg.svd(channel, full_matrices=False)
    s[compression:] = 0
    return np.dot(u * s, vh)

if __name__ == "__main__":
    # Opens an image in RGB "tuples" [(143, 35, 29), (255, 115, 0) ... ]
    print("opening image")
    pic = Image.open(image_file)
    pix = np.array(pic)
    print(pix.shape)
    print("Got Pixel Array")
    # Need to get each red
    print("Red channel")
    red = compress_channel(pix[:,:,0])

    print("Green channel")
    green = compress_channel(pix[:,:,1])

    print("Blue channel")
    blue = compress_channel(pix[:,:,2])

    pix[:,:,0] = red
    pix[:,:,1] = green
    pix[:,:,2] = blue
    print("Saving")
    Image.fromarray(pix).save("result.png")
