import tkinter as tk
from tkinter import ttk

class GraphFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text='Graph')
        label.pack(side='top', padx=10, pady=10, fill='both', expand=True)
        
class CameraFeedFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text='Camera Feed')
        label.pack(side='top', padx=10, pady=10, fill='both', expand=True)


class ControlFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text='Control')
        label.pack(side='top', padx=10, pady=10, fill='both', expand=True)

