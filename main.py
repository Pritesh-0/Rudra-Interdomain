import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainApp(tk.Frame):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cave Wall Climbing Robot")
        
        self.set_border_width(10)
        self.set_default_size(800, 600)
        #self.fullscreen()
        self.set_decorated(True)
        
        

if __name__ == '__main__':
    win = CaveWallClimbingRobotGui()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
