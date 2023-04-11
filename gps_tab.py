import tkinter as tk
from tkinter import ttk

class GraphFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.graph_frame = ttk.Frame(self, borderwidth=5, relief="groove")
        self.graph_frame.pack(side="left", fill="both", expand=True)
        
        self.graph_container = ttk.Frame(self.graph_frame)
        self.graph_container.pack(fill="both", expand=True, padx=3, pady=3)
        
        self.graph_label = tk.Label(self.graph_container, text="Graph")
        self.graph_label.pack(fill="both", expand=True)

class CameraFeedFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.camerafeed_frame = ttk.Frame(self, borderwidth=5, relief="groove")
        self.camerafeed_frame.pack(side="left", fill="both", expand=True)
        
        self.camerafeed_container = ttk.Frame(self.camerafeed_frame)
        self.camerafeed_container.pack(fill="both", expand=True, padx=3, pady=3)
        
        self.camerafeed_label = tk.Label(self.camerafeed_container, text="Camera Feed")
        self.camerafeed_label.pack(fill="both", expand=True)

class ControlFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.control_frame = ttk.Frame(self, borderwidth=5, relief="groove")
        self.control_frame.pack(side="left", fill="both", expand=True)
        
        self.control_container = ttk.Frame(self.control_frame)
        self.control_container.pack(fill="both", expand=True, padx=3, pady=3)
        
        self.control_label = tk.Label(self.control_container, text="Control")
        self.control_label.pack(fill="both", expand=True)

