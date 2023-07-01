import cv2
from PIL import Image
import numpy as np

ASCII_CHARS = '@%#*+=-:. '

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 32]
    return ascii_str

def play_ascii_video(video_path, new_width=100):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_resized = resize_image(image_pil, new_width)
        image_grayscale = grayscale_image(image_resized)
        ascii_str = pixels_to_ascii(image_grayscale)
        img_width = image_grayscale.width

        ascii_img = ''
        for i in range(0, len(ascii_str), img_width):
            ascii_img += ascii_str[i:i+img_width] + '\n'

        print(ascii_img)
        print('\033c', end='')  # Clear console for each frame

    cap.release()

# Example usage:
video_path = 'path/to/your/video.mp4'
play_ascii_video(video_path)
