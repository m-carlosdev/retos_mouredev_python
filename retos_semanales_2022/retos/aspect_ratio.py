#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
#  *   mouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.

import urllib.request as req
from PIL import Image
from math import gcd
# import numpy as np
# import cv2 as cv


IMAGE_URL = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
IMAGE_2 = "https://cnnespanol.cnn.com/wp-content/uploads/2016/09/meme-anonimo2.jpg?quality=100&strip=info&w=320&h=240&crop=1"
IMAGE_3 = "https://cdn2.mediotiempo.com/uploads/media/2023/07/21/memes-de-perros-twitter.jpg"
IMAGE_4 = "https://i.pinimg.com/originals/71/9e/80/719e80760999b4c355a723224120eb07.png"

# show image with openCV

# image_response = req.urlopen(IMAGE_URL)
# image_array = np.array(bytearray(image_response.read()))
# img = cv.imdecode(image_array, 1)
# cv.imshow('URL IMAGE', img)
# cv.waitKey()

# show image with pillow

def aspectRatio(image_url: str) -> None:
    try:
        image_response = req.urlopen(image_url)
        img = Image.open(image_response)
        width, heigth = img.size
        gcd_ratio = gcd(width, heigth)
        print(str(width//gcd_ratio) + ":" + str(heigth//gcd_ratio))
        return
    except Exception:
        return

if __name__ == "__main__":
    aspectRatio(IMAGE_URL)
    aspectRatio(IMAGE_2)
    aspectRatio(IMAGE_3)
    aspectRatio(IMAGE_4)
