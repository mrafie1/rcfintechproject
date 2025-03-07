# Testing Gen-Ai
# Make sure you have pip installed, then download google-genai

from google import genai


client = genai.Client(api_key="AIzaSyA20E9DwFOd0Z5Rp2KwueG6I9w3VnkaDSU")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)

chat = client.chats.create(model="gemini-2.0-flash")


def get_user_input():
    return input("You: ")


def get_response():
    user_input = get_user_input()
    model_response = chat.send_message(user_input)
    print(model_response.text)
    return model_response

# history = []


# while True:
    # user_input = get_user_input()
    # model_response = chat.send_message(user_input)
    # print(model_response.text)

    # history.append({"role": "user", "parts": [user_input]})
    # history.append({"role": "model", "parts": [model_response.text]})
    # print(history)
