"""App page"""

import tkinter as tk

class MyApp(tk.Frame):

    def __init__(self, root):

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
        self.create_pager()

    def create_page_container(self):
        self.page_container = tk.Frame(
            self.main_frame,
            background=self.colour1
        )

        self.page_container.columnconfigure(0, weight=0)
        self.page_container.rowconfigure(0, weight=0)
        self.page_container.rowconfigure(1, weight=1)

        self.page_container.grid(column=0, row=0, sticky=tk.NSEW)

    def create_pager(self):
        self.pager = tk.Frame(
            self.main_frame,
            background=self.colour1,
            height=10,
            width=300
        )

        # Configure the grid to make the frame fill the available space
        self.pager.columnconfigure(0, weight=1)
        self.pager.columnconfigure(1, weight=1)
        self.pager.rowconfigure(0, weight=0)
        self.pager.rowconfigure(1, weight=1)
        self.pager.grid(column=0, row=0, sticky=tk.NS)
        self.pager.grid_propagate(False)

        # Add some space between the button and the top row
        inquiries_button = tk.Button(
            self.pager,
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
            state=tk.DISABLED
        )
        # Added padding (both vertical and horizontal)
        inquiries_button.grid(column=0, row=1, padx=10, pady=20)

        self.page_number = tk.Label(
            self.pager,
            background=self.colour1,
            foreground=self.colour3,
            font=("Arial", 10)  # Can change
        )
        self.page_number.grid(column=0, row=0, pady=5)

        wanttoreturn_button = tk.Button(
            self.pager,
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
            state=tk.DISABLED
        )

        # Added padding (both vertical and horizontal)
        wanttoreturn_button.grid(column=1, row=1, padx=10, pady=20)

root = tk.Tk()
root.title('My App')
root.geometry("500x700")
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()
