import tkinter as tk
import tkinter.font as tkfont


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.winfo_toplevel().title("Tkinter Beispiel GUI")

        self.grid(padx=5, pady=5)

        tk.Label(self, text="Lass dich begrüssen").grid(column=0, row=0)
        tk.Label(self, text="Wie ist dein Name?").grid(column=0, row=1)
        self.name_widget = tk.Entry(self)
        self.name_widget.grid(column=1, row=1)
        self.name_var = tk.StringVar()
        self.name_widget["textvariable"] = self.name_var

        self.greet_button = tk.Button(self, text="Begrüsse", command=self.greet_user)
        self.greet_button.grid(column=0, row=2, columnspan=2)

        self.greeting_output = tk.Label(self, text="")
        self.greeting_output.grid(column=0, row=3, columnspan=2)

    def greet_user(self):
        user_name = self.name_var.get()
        self.greeting_output.configure(text=f"Hello {user_name}")
        

if __name__ == "__main__":
    root = tk.Tk()
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=14)
    root.option_add("*Font", default_font)

    myapp = App(root)

    myapp.mainloop()
