"""App page"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from image import analyze_image
import chatbox


class MyApp(tk.Frame):

    def __init__(self, root):

        self.current_page_index = 0
        self.pages = [self.page1, self.page2, self.page3]

        self.colour1 = "#f6f1e5"
        self.colour2 = "#203655"
        self.colour3 = "#d9c1a1"
        self.colour4 = "WHITE"

        super().__init__(
            root,
            bg = self.colour1
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()


    def upload_action(self):
        img_path = askopenfilename()
        im = Image.open(img_path)
        print(analyze_image(im))


    def load_main_widgets(self):
        self.create_page_container()
        # self.create_pager()
        self.pages[self.current_page_index]()

    def clear_frame(self, frame):
        for child in frame.winfo_children():
            child.destroy()

    def create_page_container(self):
        self.page_container = tk.Frame(
            self.main_frame,
            background=self.colour1
        )

        self.page_container.columnconfigure(0, weight=1)
        self.page_container.columnconfigure(1, weight=1)
        self.page_container.rowconfigure(0, weight=0)
        self.page_container.rowconfigure(1, weight=1)
        self.page_container.grid(column=0, row=0, sticky=tk.NS)


    def change_page(self, page_index):
        self.clear_frame(self.page_container)
        self.current_page_index = page_index
        self.pages[self.current_page_index]()

    def page1(self): #main page
        self.clear_frame(self.page_container)

        title = tk.Label(
            self.page_container,
            background = self.colour1,
            foreground = "#cd8b94",
            height = 2,
            font = ('ms serif', 35, "bold"),
            text = "SnapBack"
        )

        title.grid(column = 0, row = 0)

        text = ('Main Page')

        content = tk.Label(
            self.page_container,
            background=self.colour3,
            foreground=self.colour2,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Times', 18, "bold"),
            text=text,
            wraplength=600
        )

        content.grid(column = 1, row = 0, sticky=tk.NSEW, padx = 20, pady = 30)


        # Add some space between the button and the top row
        inquiries_button = tk.Button(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground=self.colour4,
            highlightthickness=0,
            height=3,
            width=15,
            relief=tk.FLAT,
            font=('Times', 18, "bold"),  # Can change
            cursor='hand1',
            text="Any inquiries",
            # state=tk.DISABLED
            command=lambda: self.change_page(1)
        )
        # Added padding (both vertical and horizontal)
        inquiries_button.grid(column=0, row=1, padx=10, pady=20)

        wanttoreturn_button = tk.Button(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground=self.colour4,
            highlightthickness=0,
            height=3,
            width=15,
            relief=tk.FLAT,
            font=('Times', 18, "bold"),  # Can change
            cursor='hand1',
            text="Refund / Return",
            # state=tk.DISABLED,
            command=lambda: self.change_page(2)
        )

        # Added padding (both vertical and horizontal)
        wanttoreturn_button.grid(column=1, row=1, padx=10, pady=20)

    def page2(self): #Inquiry chatbox page
        # title = tk.Label(
        #     self.page_container,
        #     background=self.colour1,
        #     foreground=self.colour2,
        #     height=2,
        #     font=('Times', 26, "bold"),
        #     text="page 2"
        # )
        #
        # title.grid(column=0, row=0)
        #
        # text = ('Inquiry ChatBox')
        #
        # content = tk.Label(
        #     self.page_container,
        #     background=self.colour3,
        #     foreground=self.colour2,
        #     justify=tk.LEFT,
        #     anchor=tk.N,
        #     pady=20,
        #     font=('Times', 18, "bold"),
        #     text=text,
        #     wraplength=600
        # )
        #
        # content.grid(column = 1, row = 0, sticky=tk.NSEW, padx = 30, pady = 30)
        #
        # self.return_button()

        self.clear_frame(self.page_container)

        # Create a frame to hold the chatbox
        self.chat_frame = tk.Frame(self.page_container, bg=self.colour3)
        self.chat_frame.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW, padx=20, pady=20)

        # Expand chatbox properly
        self.chat_frame.columnconfigure(0, weight=1)
        self.chat_frame.rowconfigure(0, weight=1)

        # Initialize and pack chatbox
        self.chat_app = chatbox.ChatApplication(self.chat_frame)
        self.chat_app.run()

        self.return_button()

    def page3(self): #return analysis page
        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour2,
            height=2,
            font=('Times', 26, "bold"),
            text="page 3"
        )

        title.grid(column=0, row=0)

        text = ('Return Page')

        content = tk.Label(
            self.page_container,
            background=self.colour3,
            foreground=self.colour2,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Times', 18, "bold"),
            text=text,
            wraplength=600
        )

        content.grid(column = 1, row = 0, sticky=tk.NSEW, padx = 30, pady = 30)

        upload_image = tk.Button(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground=self.colour4,
            highlightthickness=0,
            height=3,
            width=15,
            relief=tk.FLAT,
            font=('Times', 18, "bold"),  # Can change
            cursor='hand1',
            text="Upload Image",
            # state=tk.DISABLED,
            command=lambda: self.upload_action()
        )

        upload_image.grid(column=0, row=1, padx=10, pady=20)

        self.return_button()

    def return_button(self):
        return_button = tk.Button(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground=self.colour4,
            highlightthickness=0,
            height=2,
            width=10,
            relief=tk.FLAT,
            font=('Times', 13, "bold"),  # Can change
            cursor='hand1',
            text="Back",
            # state=tk.DISABLED
            command=lambda: self.change_page(0)
        )
        # Added padding (both vertical and horizontal)
        return_button.grid(column=1, row=2, padx=10, pady=50, sticky=tk.E)

root = tk.Tk()
root.title('My App')
root.geometry("500x700")
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()
