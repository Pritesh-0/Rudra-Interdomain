import tkinter as tk
from tkinter import ttk
from tabs import *

class MainApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Cave Wall Climbing Robot GUI")
        
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.pack(fill='both', expand=True)
        
        self.tab1 = GPSTab(self.notebook)
        self.tab2 = StandardTab(self.notebook)
        self.tab3 = SettingsTab(self.notebook)
        self.tab4 = LogsTab(self.notebook)
        
        self.notebook.add(self.tab1, text='GPS')
        self.notebook.add(self.tab2, text='Standard')
        self.notebook.add(self.tab3, text='Settings')
        self.notebook.add(self.tab4, text='Logs')

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.pack(fill='both', expand=True)
    root.mainloop()
