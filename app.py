"""App page"""

import tkinter as tk

class MyApp(tk.Frame):

    def __init__(self, root):

        self.current_page_index = 0
        self.pages = [self.page1, self.page2, self.page3]

        self.colour1 = "#F3DDD5"
        self.colour2 = "#DCE1D4"
        self.colour3 = "WHITE"
        self.colour4 = "#A4B8AC"

        super().__init__(
            root,
            bg = self.colour1
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()

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

    def page1(self):
        self.clear_frame(self.page_container)

        title = tk.Label(
            self.page_container,
            background = self.colour1,
            foreground = self.colour3,
            height = 2,
            font = ('Axial', 26, "bold"),
            text = "page 1"
        )

        title.grid(column = 0, row = 0)

        text = ('hi')

        content = tk.Label(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=("Arial", 16),
            text=text,
            wraplength=600
        )

        content.grid(column = 1, row = 0, sticky=tk.NSEW, padx = 20)


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
            font=('Arial', 15),  # Can change
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
            font=('Arial', 15),  # Can change
            cursor='hand1',
            text="Want to Return",
            # state=tk.DISABLED,
            command=lambda: self.change_page(2)
        )

        # Added padding (both vertical and horizontal)
        wanttoreturn_button.grid(column=1, row=1, padx=10, pady=20)

    def page2(self):
        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Axial', 26, "bold"),
            text="page 2"
        )

        title.grid(column=0, row=0)

        text = ('hihi')

        content = tk.Label(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=("Arial", 16),
            text=text,
            wraplength=600
        )

        content.grid(column=0, row=0, sticky=tk.NSEW)

    def page3(self):
        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Axial', 26, "bold"),
            text="page 3"
        )

        title.grid(column=0, row=0)

        text = ('hihihi')

        content = tk.Label(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=("Arial", 16),
            text=text,
            wraplength=600
        )

        content.grid(column=0, row=0, sticky=tk.NSEW)

root = tk.Tk()
root.title('My App')
root.geometry("500x700")
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()
