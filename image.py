from google import genai
from google.genai import types


import PIL.Image

image = PIL.Image.open('2c2w6dn.jpg')

client = genai.Client(api_key="AIzaSyA20E9DwFOd0Z5Rp2KwueG6I9w3VnkaDSU")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Is this product returnable or no? Answer with either Returnable or Unreturnable", image])

answer = response.text
print(answer)
