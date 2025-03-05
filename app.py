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
        self.main_frame.pack(fill=tk.BOTH, expand = True)
        self.main_frame.columnconfigure(0, weight = 1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()

    def load_main_widgets(self):
        self.create_page_container()
        self.create_pager()

    def create_page_container(self):
        self.page_container = tk.Frame(
            self.main_frame,
            background = self.colour1
        )

        self.page_container.columnconfigure(0, weight = 0)
        self.page_container.rowconfigure(0, weight = 0)
        self.page_container.rowconfigure(1, weight = 1)

        self.page_container.grid(column = 0, row=0, sticky = tk.NSEW)

    def create_pager(self):
        self.pager = tk.Frame(
            self.main_frame,
            background = self.colour1,
            height = 125,
            width = 400
        )

        self.pager.columnconfigure(1,weight=1)
        self.pager.rowconfigure(0, weight=1)
        self.pager.grid(column=0, row=1, sticky=tk.NS)
        self.pager.grid_propagate(False)

        inquiries_button = tk.Button(
            self.pager,
            background = self.colour2,
            foreground = self.colour3,
            activebackground = self.colour2,
            activeforeground = self.colour3,
            disabledforeground = self.colour4,
            highlightthickness = 0,
            width = 10,
            relief = tk.FLAT,
            font = ('Arial', 10), #can change
            cursor = 'hand1',
            text = "Any inquiries",
            state=tk.DISABLED

        )

        inquiries_button.grid(column = 0, row=0)

        self.page_number = tk.Label(
            self.pager,
            background = self.colour1,
            foreground = self.colour3,
            font = ("Arial", 10) #can change
        )

        self.page_number.grid(column = 1, row = 0)

        wanttoreturn_button = tk.Button(
            self.pager,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground=self.colour4,
            highlightthickness=0,
            width=10,
            relief=tk.FLAT,
            font=('Arial', 10),  # can change
            cursor='hand1',
            text="Want to Return",
            state=tk.DISABLED

        )

        wanttoreturn_button.grid(column=2, row=0)



root = tk.Tk()
root.title('My App')
root.geometry("700x500")
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()
