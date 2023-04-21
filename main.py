import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from tabs import Graph


class MainApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cave Wall Climbing Robot")
        
        self.set_border_width(10)
        self.set_default_size(800, 600)
        #self.fullscreen()
        self.set_decorated(True)
        
        graph_gui = Graph()
        graph_frame = graph_gui.graph_container.get_parent()
        graph_frame.remove(graph_gui.graph_container)
        self.add(graph_gui.graph_container)
        
        

if __name__ == '__main__':
    win = MainApp()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
