from google import genai
import tkinter as tk
from PIL import Image, ImageTk, UnidentifiedImageError


import PIL.Image


def analyze_image(img):

    image = img

    client = genai.Client(api_key="AIzaSyA20E9DwFOd0Z5Rp2KwueG6I9w3VnkaDSU")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Is this product returnable or no? Answer with either Returnable or Unreturnable", image])

    answer = response.text
    return answer
