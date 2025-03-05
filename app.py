"""App page"""

import tkinter as tk

class MyApp(tk.Frame):

    def __int__(self, root):

        self.colour1 = "#F4DDD5"
        self.colour2 = "#DCE1DA"
        self.colour3 = "WHITE"

        super().__init__(
            root,
            bg = self.colour1
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand = True)
        self.main_frame.columnconfigure(0, weight = 1)
        self.main_frame.rowconfigure(0, weight=1)

root = tk.Tk()
root.title('My App')
root.geometry("700x500")
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()
