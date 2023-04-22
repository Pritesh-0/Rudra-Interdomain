import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg
from matplotlib.figure import Figure
import numpy as np
from gi.repository import Gtk


class SingleGraph(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

        self.canvas = FigureCanvasGTK3Agg(self.fig)
        self.pack_start(self.canvas, True, True, 0)

    def set_size_request(self, width, height):
        Gtk.Box.set_size_request(self, width, height)
        self.canvas.set_size_request(width, height)

