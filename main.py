# Testing Gen-Ai
# Make sure you have pip installed, then download google-genai

from google import genai
# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)



# client = genai.Client(api_key="AIzaSyA20E9DwFOd0Z5Rp2KwueG6I9w3VnkaDSU")
# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works"
# )
# print(response.text)
#
# chat = client.chats.create(model="gemini-2.0-flash")
#
# history = []


# while True:
#     user_input = input("You: ")
#     model_response = chat.send_message(user_input)
#     print(model_response.text)
#
#     history.append({"role": "user", "parts": [user_input]})
#     history.append({"role": "model", "parts": [model_response.text]})
#     # print(history)
