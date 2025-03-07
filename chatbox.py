"""Chatbox"""

from tkinter import *
import google.generativeai as genai

genai.configure(api_key="AIzaSyA20E9DwFOd0Z5Rp2KwueG6I9w3VnkaDSU")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

COLOUR1 = "#f6f1e5"
COLOUR2 = "#203655"
COLOUR3 = "#d9c1a1"
COLOUR4 = "WHITE"
COLOUR5 = "#825855"

FONT = "Times 14"
FONT_BOLD = "Times 13 bold"


class ChatApplication:
    def __init__(self, parent):
        # self.window = Tk()
        # self._setup_main_window()
        self.window = parent  # Set the parent frame instead of Tk()
        self._setup_main_window()

    def run(self):
        # self.window.mainloop()
        pass

    def _setup_main_window(self):
        # self.window.title("Chat")
        # self.window.resizable(width = False, height = False)
        self.window.configure(width=470, height=550, bg=COLOUR3)

        # head label
        head_label = Label(self.window, bg="#e8e2e1", fg="#cd8b94",
                           text="SnapBack", font="STIX 20 bold", pady=10)
        # head_label.place(relwidth=1)
        head_label.pack(fill=X)

        # tiny divider
        line = Label(self.window, width=450, bg=COLOUR1)
        # line.place(relwidth=1, rely=0.07, relheight=0.012)
        line.pack(fill=X, pady=(0, 5))

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=COLOUR3, fg=COLOUR1,
                                font=FONT, padx=5, pady=5)
        # self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.pack(fill=BOTH, expand=True, pady=(0, 5))
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        # scrollbar.place(relheight=1, relx=0.974)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=COLOUR1, height=80)
        # bottom_label.place(relwidth=1, rely=0.825)
        bottom_label.pack(fill=X, pady=(5, 0))

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=COLOUR4, fg=COLOUR2, font=FONT)
        # self.msg_entry.place(relwidth=0.74, relheight=0.06, rely= 0.008, relx=0.011)
        self.msg_entry.pack(side=LEFT, fill=X, expand=True, padx=(10, 5), pady=10)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=10, bg="#e8e2e1",
                             command=self._on_send_pressed)
        # send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        send_button.pack(side=RIGHT, padx=(5, 10), pady=10)

    def _on_enter_pressed(self, _event):
        self._on_send_pressed()

    def _on_send_pressed(self):
        msg = self.msg_entry.get().strip()
        if msg:
            self._insert_message(msg, "You")
            self.msg_entry.delete(0, END)
            self._get_ai_response(msg)

    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, f"{sender}: {msg}\n\n", "user")
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # Auto-scroll

    def _get_ai_response(self, user_msg):
        response = chat.send_message(user_msg)
        ai_msg = response.text.strip()
        self._insert_message(ai_msg, "AI")
