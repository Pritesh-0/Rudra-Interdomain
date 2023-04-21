import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from tabs import *


class MainApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cave Wall Climbing Robot")
        
        self.set_border_width(10)
        self.set_default_size(800, 600)
        #self.fullscreen()
        self.set_decorated(True)
        
        #graph_gui = Graph()
        #camerafeed_gui = CameraFeed()
        control_gui = Controls()
        status_gui = Status()
        log_gui = Log()
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        #box.pack_start(camerafeed_gui.camerafeed_frame, True, True, 0)
        #box.pack_start(graph_gui.graph_frame, True, True, 0)
        box.pack_start(control_gui.controls_frame, True, True, 0)
        box.pack_start(status_gui.status_frame, True, True, 0)
        box.pack_start(log_gui.log_frame, True, True, 0)
        
        
        self.add(box)
        

if __name__ == '__main__':
    win = MainApp()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
