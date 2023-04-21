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

