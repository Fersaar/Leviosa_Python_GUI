#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jul 05, 2020 12:03:42 PM CEST  platform: Windows NT
#    Jul 05, 2020 12:15:56 PM CEST  platform: Windows NT
#    Jul 05, 2020 05:33:07 PM CEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global kd
    kd = tk.DoubleVar()
    global kp
    kp = tk.DoubleVar()
    global ki
    ki = tk.DoubleVar()
    global PoM
    PoM = tk.BooleanVar()
    global nullpunkt_offset
    nullpunkt_offset = tk.IntVar()
    global overwrite0
    overwrite0 = tk.IntVar()
    global overwrite1
    overwrite1 = tk.IntVar()
    global overwrite2
    overwrite2 = tk.IntVar()
    global overwrite3
    overwrite3 = tk.IntVar()
    global overwrite_gnd
    overwrite_gnd = tk.IntVar()
    global sollwert
    sollwert = tk.IntVar()


def btn_send_sollwert():
    message = "00"+ "%6.0f" % (sollwert.get()) + "%";
    s.sendSerialData(message)
    print('befehle_gui_support.btn_send_sollwert')
    sys.stdout.flush()

def btn_send_fullon():
    message = "07" + "%";
    s.sendSerialData(message)
    print('befehle_gui_support.btn_send_fullon')
    sys.stdout.flush()

def btn_send_nullpunkt_offset():
    message = "01" + "%6.2f" % (nullpunkt_offset.get()) + "%";
    s.sendSerialData(message)
    sys.stdout.flush()

def btn_send_off():
    message = "05" + "%";
    s.sendSerialData(message)
    print('befehle_gui_support.btn_send_off')
    sys.stdout.flush()

def btn_send_offsweep():
    message = "06" + "%";
    s.sendSerialData(message)
    print('befehle_gui_support.btn_send_offsweep')
    sys.stdout.flush()

def btn_send_overwrite():
    message = "03" + "%6.0f%6.0f%6.0f%6.0f%6.0f" % (overwrite0.get(),overwrite1.get(),overwrite2.get(),overwrite3.get(),overwrite_gnd.get()) + "%"
    s.sendSerialData(message)
    print('befehle_gui_support.btn_send_overwrite')
    sys.stdout.flush()

def btn_send_pid_values():
    message = "02" + "%6.2f%6.2f%6.2f%6.0f" % (kp.get(), ki.get(), kd.get(), not PoM.get()) +"%"
    s.sendSerialData(message)
    print('befehle_gui_support.btn_send_pid_values')
    sys.stdout.flush()

def btn_set_automatic():
    message = "04" + "%";
    s.sendSerialData(message)
    print('befehle_gui_support.btn_set_automatic')
    sys.stdout.flush()

def init(top, gui,SerialReference, *args, **kwargs):
    global w, top_level, root, s
    s = SerialReference
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import befehle_gui
    befehle_gui.vp_start_gui()




