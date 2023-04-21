import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Graph(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Graph Window")

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.main_box)
        graph_frame = Gtk.Frame(label="Graph Frame")
        self.main_box.pack_start(graph_frame, True, True, 0)

        self.graph_container = Gtk.Box()
        graph_frame.add(self.graph_container)
        graph_frame.set_size_request(400, 400)
        graph_label = Gtk.Label(label="Graph")
        self.graph_container.pack_start(graph_label, True, True, 0)

