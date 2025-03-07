"""App page"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from image import analyze_image
import chatbox
import webbrowser_open


class MyApp(tk.Frame):

    def __init__(self, root):

        self.current_page_index = 0
        self.pages = [self.page1, self.page2, self.page3, self.page4, self.page5, self.page6, self.page7]

        self.colour1 = "#f6f1e5"
        self.colour2 = "#203655"
        self.colour3 = "#d9c1a1"
        self.colour4 = "WHITE"

        super().__init__(
            root,
            bg=self.colour1
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()


    def upload_action(self):
        img_path = askopenfilename()
        im = Image.open(img_path)
        # print(analyze_image(im))
        answer = analyze_image(im)
        if answer == "Returnable":
            self.change_page(3)
        else:
            self.change_page(4)


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

    def page1(self): # main page
        self.clear_frame(self.page_container)

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground="#cd8b94",
            height=2,
            font=('ms serif', 35, "bold"),
            text="SnapBack"
        )

        title.grid(column=0, row=0)

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

        content.grid(column=1, row=0, sticky=tk.NSEW, padx=20, pady=30)


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

    def page2(self): # Inquiry chatbox page

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

    def page3(self): # return analysis page
        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground="#cd8b94",
            height=2,
            font=('ms serif', 35, "bold"),
            text="SnapBack"
        )

        title.grid(column=0, row=0)

        text = ('Snap. Return. Done!')

        content = tk.Label(
            self.page_container,
            background=self.colour3,
            foreground=self.colour2,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Times', 16, "bold"),
            text=text,
            wraplength=600
        )

        content.grid(column=1, row=0, sticky=tk.NSEW, padx=30, pady=30)

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

        upload_image.grid(column=1, row=1, padx=10, pady=20)

        self.return_button()

    def page4(self): # returnable page
        for widget in self.page_container.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground="#cd8b94",
            height=2,
            font=('ms serif', 35, "bold"),
            text="SnapBack"
        )

        title.grid(column=0, row=0, columnspan = 2, sticky="ew", pady=(10,20))

        text = ('Looks good! You can return this.')

        content = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour2,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Times', 18, "bold"),
            text=text,
            wraplength=600
        )

        content.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=20, pady=(0,30))

        continue_return = tk.Button(
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
            text="Continue Returning",
            # state=tk.DISABLED,
            command=lambda: self.upload_action()
        )

        continue_return.grid(column=0, row=2, columnspan=2, pady=(0,10))

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
        return_button.grid(column=0, row=3, columnspan=2, pady=(10,20), sticky="e")

        self.page_container.grid_columnconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(1, weight=1)
        self.page_container.grid_rowconfigure(1, weight=1)
        # self.return_button()

    def page5(self): # unreturnable page
        # Clear the page container before adding new widgets
        for widget in self.page_container.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground="#cd8b94",
            height=2,
            font=('ms serif', 35, "bold"),
            text="SnapBack"
        )

        title.grid(column=0, row=0, columnspan=2, sticky="ew", pady=(10,20))

        text = ('Oops, we noticed some issues in the photo...')

        content = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour2,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Times', 18, "bold"),
            text=text,
            wraplength=600
        )

        content.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=20, pady=(0,30))

        resale = tk.Button(
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
            text="Resale",
            # state=tk.DISABLED,
            command=lambda: self.change_page(5)
        )

        resale.grid(column=0, row=2, padx=10, pady=10)

        donate = tk.Button(
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
            text="Donate",
            # state=tk.DISABLED,
            command=lambda: self.change_page(6)
        )

        donate.grid(column=1, row=2, padx=10, pady=10)

        try_again = tk.Button(
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
            text="Try Again",
            # state=tk.DISABLED,
            command=lambda: self.upload_action()
        )

        try_again.grid(column=0, row=3, columnspan=2, padx=10, pady=(10,20))

        self.page_container.grid_columnconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(1, weight=1)
        self.page_container.grid_rowconfigure(1, weight=1)
        # self.return_button()

    def page6(self): # resale page
        # Clear the page container before adding new widgets
        for widget in self.page_container.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground="#cd8b94",
            height=2,
            font=('ms serif', 35, "bold"),
            text="SnapBack"
        )

        title.grid(column=0, row=0, columnspan=2, sticky="ew", pady=(10,20))

        text = ('Resale Page')

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

        content.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=20, pady=(0,10))

        text = ('Our suggested value: $50')

        content = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour2,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Times', 18, "bold"),
            text=text,
            wraplength=600
        )

        content.grid(column=0, row=2, columnspan=2, sticky="nsew", padx=20, pady=(0,20))

        facebook = tk.Button(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground=self.colour4,
            highlightthickness=0,
            height=3,
            width=18,
            relief=tk.FLAT,
            font=('Times', 18, "bold"),  # Can change
            cursor='hand1',
            text="Facebook Marketplace",
            # state=tk.DISABLED,
            command=lambda: webbrowser_open.open("https://www.facebook.com/marketplace/")
        )

        facebook.grid(column=0, row=3, columnspan=2, pady=(0,10))

        ebay = tk.Button(
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
            text="eBay",
            # state=tk.DISABLED,
            command=lambda: webbrowser_open.open("https://www.ebay.ca/")
        )

        ebay.grid(column=0, row=4, columnspan=2, pady=(0,10))

        poshmark = tk.Button(
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
            text="Poshmark",
            # state=tk.DISABLED,
            command=lambda: webbrowser_open.open("https://poshmark.com/")
        )

        poshmark.grid(column=0, row=5, columnspan=2, pady=(0,20))

        self.page_container.grid_columnconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(1, weight=1)
        self.page_container.grid_rowconfigure(1, weight=1)
        self.page_container.grid_rowconfigure(2, weight=1)
        self.page_container.grid_rowconfigure(3, weight=1)
        self.page_container.grid_rowconfigure(4, weight=1)
        self.page_container.grid_rowconfigure(5, weight=1)

    def page7(self): # donate page
        # Clear the page container before adding new widgets
        for widget in self.page_container.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground="#cd8b94",
            height=2,
            font=('ms serif', 35, "bold"),
            text="SnapBack"
        )

        title.grid(column=0, row=0, columnspan=2, sticky="ew", pady=(10,20))

        text = ('Donate Page')

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

        content.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=20, pady=(0,30))

        self.page_container.grid_columnconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(1, weight=1)
        self.page_container.grid_rowconfigure(1, weight=1)

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
