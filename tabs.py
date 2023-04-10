import tkinter as tk
from tkinter import ttk
from gps_tab import *

class GPSTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        graph_frame = GraphFrame(self)
        camera_feed_frame = CameraFeedFrame(self)
        control_frame = ControlFrame(self)

        graph_frame.grid(row=0, column=0, rowspan=2, sticky='nsew')
        camera_feed_frame.grid(row=0, column=1, sticky='nsew')
        control_frame.grid(row=1, column=1, sticky='nsew')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
class StandardTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.angle_label = tk.Label(self, text='Stats;AnalyzedData;')
        self.angle_label.pack(side='left', padx=10, pady=10)

        self.angle_value = tk.Label(self, text='2')
        self.angle_value.pack(side='left', padx=10, pady=10)

class SettingsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.speed_label = tk.Label(self, text='ConfigSettings;FAilSafes')
        self.speed_label.pack(side='left', padx=10, pady=10)

        self.speed_value = tk.Label(self, text='2')
        self.speed_value.pack(side='left', padx=10, pady=10)
        
class LogsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.log_text = tk.Text(self)
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)

        self.log_scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.log_text.yview)
        self.log_scrollbar.pack(side='right', fill='y')

        self.log_text.configure(yscrollcommand=self.log_scrollbar.set)


