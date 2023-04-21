import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Graph:
    def __init__(self):
        self.graph_frame = Gtk.Frame(label="Graph")
        
        graph_container = Gtk.Box()
        self.graph_frame.add(graph_container)

        graph_label = Gtk.Label(label="Graph")
        graph_container.pack_start(graph_label, True, True, 0)
        
        
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



