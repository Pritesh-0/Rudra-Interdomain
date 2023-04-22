import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from graphs import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg


class Graph:
    def __init__(self):
        self.graph_frame = Gtk.Frame(label="Graph")
        graph_container = Gtk.Box()
        self.graph_frame.add(graph_container)

        single_graph = SingleGraph()
        single_graph.set_size_request(400, 300)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(single_graph)

        graph_container.pack_start(scrolled_window, True, True, 0)


        
class CameraFeed:
    def __init__(self):
        self.camerafeed_frame = Gtk.Frame(label="Camera Feed")
        
        camerafeed_container = Gtk.Box()
        self.camerafeed_frame.add(camerafeed_container)

        camerafeed_label = Gtk.Label(label="Camera Feed")
        camerafeed_container.pack_start(camerafeed_label, True, True, 0)
        
   
class Controls:
    def __init__(self):
        self.controls_frame = Gtk.Frame(label="Controls")
        
        controls_container = Gtk.Box()
        self.controls_frame.add(controls_container)

        controls_label = Gtk.Label(label="Controls")
        controls_container.pack_start(controls_label, True, True, 0)
        
        
class Status:
    def __init__(self):
        self.status_frame = Gtk.Frame(label="Status")
        
        status_container = Gtk.Box()
        self.status_frame.add(status_container)

        status_label = Gtk.Label(label="Status")
        status_container.pack_start(status_label, True, True, 0)
        

class Log:
    def __init__(self):
        self.log_frame = Gtk.Frame(label="Log")
        log_container = Gtk.Box()
        self.log_frame.add(log_container)

        log_scroller = Gtk.ScrolledWindow()
        log_container.pack_start(log_scroller, True, True, 0)

        self.log_textview = Gtk.TextView()
        log_scroller.add(self.log_textview)

    def add(self, message):
        self.log_textview.get_buffer().insert_at_cursor(message + "\n")






