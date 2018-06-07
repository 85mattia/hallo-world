import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk
import RPi.GPIO as Gpio
import serial
import time
import threading
import subprocess    
import os
import urllib.request
import urllib.error

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
        self.label2.set_text("updatato")
        self.currentFolder = os.getcwd()
           
        
    
    def buttonPressed(self,button):
        GObject.idle_add(self.startSpinner)
        GObject.idle_add(self.updateProcess)
        
    def updateProcess(self):
        try:
            urllib.request.urlopen("https://www.google.com", timeout=1)
            print("ce rete")
        except urllib.error.URLError:
            print("no ce rete")
            GObject.idle_add(self.stopSpinner)
            return
        output = subprocess.check_output(["sudo", "sh", "update.sh"])
        print(output)
        out = subprocess.check_output(["sudo", "chmod", "-R", "777", self.currentFolder])
        print(out)
        self.builder.get_object("spinner").stop()
    
    def startSpinner(self):
        self.builder.get_object("spinner").active = True
        self.builder.get_object("spinner").start()
        
    def stopSpinner(self):
        self.builder.get_object("spinner").stop()
        
        
    
        
if __name__ == "__main__":
    win = HalloWorld()
    GObject.threads_init()
    Gtk.main()
