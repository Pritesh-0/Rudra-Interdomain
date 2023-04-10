import tkinter as tk
from tkinter import ttk

class GPSFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.temp_label = tk.Label(self, text = 'CameraFeed;Graph;Control;')
        self.temp_label.pack(side='left', padx=10, pady=10)

        self.temp_value = tk.Label(self, text='3')
        self.temp_value.pack(side='left', padx=10, pady=10)
        
class StandardFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.angle_label = tk.Label(self, text='Stats;AnalyzedData;')
        self.angle_label.pack(side='left', padx=10, pady=10)

        self.angle_value = tk.Label(self, text='2')
        self.angle_value.pack(side='left', padx=10, pady=10)

class SettingsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.speed_label = tk.Label(self, text='ConfigSettings;FAilSafes')
        self.speed_label.pack(side='left', padx=10, pady=10)

        self.speed_value = tk.Label(self, text='2')
        self.speed_value.pack(side='left', padx=10, pady=10)
        
class LogsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.log_text = tk.Text(self)
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)

        self.log_scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.log_text.yview)
        self.log_scrollbar.pack(side='right', fill='y')

        self.log_text.configure(yscrollcommand=self.log_scrollbar.set)


