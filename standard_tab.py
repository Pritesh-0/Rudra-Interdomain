import tkinter as tk
from tkinter import ttk

class StatsFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.stats_frame = ttk.Frame(self, borderwidth=5, relief="groove")
        self.stats_frame.pack(side="left", fill="both", expand=True)
        
        self.stats_container = ttk.Frame(self.stats_frame)
        self.stats_container.pack(fill="both", expand=True, padx=3, pady=3)
        
        self.stats_label = tk.Label(self.stats_container, text="Stats")
        self.stats_label.pack(fill="both", expand=True)
