# Testing Gen-Ai
# Make sure you have pip installed, then download google-genai

from google import genai
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog
# from PIL import Image
#
# class App():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry('1000x2000')
#         self.root.mainloop()
#         return
#
# if __name__ == '__main__':
#     App()


client = genai.Client(api_key="AIzaSyA20E9DwFOd0Z5Rp2KwueG6I9w3VnkaDSU")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)

chat = client.chats.create(model="gemini-2.0-flash")

history = []


while True:
    user_input = input("You: ")
    model_response = chat.send_message(user_input)
    print(model_response.text)

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response.text]})
    # print(history)
