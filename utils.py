import string
import cv2
from random import sample
import codecs

def random_char():
    random_char = ''.join(sample(string.ascii_letters, 1))
    return random_char


def read_file(filename):
    with codecs.open(filename, 'r', encoding='utf8') as f:
        text = f.read()
        return text

def write_file(filename, text):
    with codecs.open(filename, 'w', encoding='utf8') as f:
        f.write(text)

def frame_resize(image, scalar=0.5):
    height, width, layers = image.shape
    resize = cv2.resize(image, (int(width * scalar), int(height * scalar)))
    return resize
