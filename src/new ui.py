import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Custom Language Interpreter")
        self.master.geometry("800x500")
        self.master.config(bg="#F5DEB3")
        self.create_widgets()

    def create_widgets(self):
        # Create a panel for the buttons
        button_panel = tk.Frame(self.master, bg="#B0C4DE", width=100)
        button_panel.pack(side=tk.LEFT, fill=tk.BOTH)

        # Define the buttons
        display_button = tk.Button(button_panel, text="display", width=10, bg="#ADD8E6")
        readnumber_button = tk.Button(button_panel, text="readnumber", width=10, bg="#ADD8E6")
        loopupto_button = tk.Button(button_panel, text="loopupto", width=10, bg="#ADD8E6")
        add_button = tk.Button(button_panel, text="add", width=10, bg="#ADD8E6")
        multiply_button = tk.Button(button_panel, text="multiply", width=10, bg="#ADD8E6")
        sub_button = tk.Button(button_panel, text="sub", width=10, bg="#ADD8E6")
        divide_button = tk.Button(button_panel, text="divide", width=10, bg="#ADD8E6")

        # Pack the buttons in the panel
        display_button.pack(side=tk.TOP, padx=10, pady=10)
        readnumber_button.pack(side=tk.TOP, padx=10, pady=10)
        loopupto_button.pack(side=tk.TOP, padx=10, pady=10)
        add_button.pack(side=tk.TOP, padx=10, pady=10)
        multiply_button.pack(side=tk.TOP, padx=10, pady=10)
        sub_button.pack(side=tk.TOP, padx=10, pady=10)
        divide_button.pack(side=tk.TOP, padx=10, pady=10)

        # Create a text box for code input and output
        self.text = tk.Text(self.master, wrap=tk.WORD, width=100, font=("Consolas", 12))
        self.text.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Bind the buttons to insert the corresponding keyword in the text box
        display_button.config(command=lambda: self.text.insert(tk.END, "display"))
        readnumber_button.config(command=lambda: self.text.insert(tk.END, "readnumber"))
        loopupto_button.config(command=lambda: self.text.insert(tk.END, "loopupto"))
        add_button.config(command=lambda: self.text.insert(tk.END, "add"))
        multiply_button.config(command=lambda: self.text.insert(tk.END, "multiply"))
        sub_button.config(command=lambda: self.text.insert(tk.END, "sub"))
        divide_button.config(command=lambda: self.text.insert(tk.END, "divide"))


#drag and drop
class DragDropWidget(tk.Label):
    def __init__(self, master, keyword, **kwargs):
        super().__init__(master, **kwargs)
        self.keyword = keyword

        self.bind('<ButtonPress-1>', self.on_drag_start)
        self.bind('<ButtonRelease-1>', self.on_drag_end)

    def on_drag_start(self, event):
        self.start_x = event.x_root
        self.start_y = event.y_root

    def on_drag_end(self, event):
        x = event.x_root - self.start_x + self.winfo_x()
        y = event.y_root - self.start_y + self.winfo_y()
        self.master.create_text_box(self.keyword, x, y)


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title('My Interpreter')

        self.create_widgets()

    def create_widgets(self):
        self.text_box = tk.Text(self.master)
        self.text_box.pack()

        self.keywords_frame = tk.Frame(self.master)
        self.keywords_frame.pack(side='left')

        keywords = ['display', 'readnumber', 'loopupto', 'add', 'multiply', 'sub', 'divide', 'define function', 'if']

        for i, keyword in enumerate(keywords):
            label = DragDropWidget(self.keywords_frame, keyword, text=keyword, bg='gray')
            label.grid(row=i, column=0, pady=5, padx=10, sticky='w')

    def create_text_box(self, keyword, x, y):
        self.text_box.focus()
        self.text_box.mark_set(tk.INSERT, f"{y}.{x}")
        self.text_box.insert(tk.INSERT, keyword + ' ')

root = tk.Tk()
app = Application(master=root)
app.mainloop()




