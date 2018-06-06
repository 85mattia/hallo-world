import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk
import RPi.GPIO as Gpio
import serial
import time
import threading
import subprocess

class HalloWorld(Gtk.Window):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui-home.glade")
        self.builder.connect_signals(self)
        self.label1 = self.builder.get_object("label1")
        self.label2 = self.builder.get_object("label2")
        self.window = self.builder.get_object("window")
        self.window.set_position(Gtk.WindowPosition.CENTER) 
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()
        self.label2.set_text("ora funzia dopo restart")
        
    
    def buttonPressed(self,button):
        output = subprocess.check_output(["sudo", "sh", "update.sh"])
        print(output)
        
    
        
if __name__ == "__main__":
    win = HalloWorld()
    GObject.threads_init()
    Gtk.main()
