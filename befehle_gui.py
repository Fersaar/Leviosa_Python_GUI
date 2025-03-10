#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Aug 07, 2020 11:58:01 AM CEST  platform: Windows NT

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

import befehle_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    befehle_gui_support.set_Tk_var()
    top = Toplevel1 (root)
    befehle_gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    befehle_gui_support.set_Tk_var()
    top = Toplevel1 (w)
    befehle_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("824x352+520+339")
        top.minsize(140, 1)
        top.maxsize(3844, 1057)
        top.resizable(1, 1)
        top.title("Befehle")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#ffffff")
        top.configure(highlightcolor="black")

        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.024, rely=0.028, relheight=0.327
                , relwidth=0.267)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Sollwerte''')

        self.TEntry1 = ttk.Entry(self.TLabelframe1)
        self.TEntry1.place(relx=0.364, rely=0.435, relheight=0.217, relwidth=0.3
                , bordermode='ignore')
        self.TEntry1.configure(textvariable=befehle_gui_support.nullpunkt_offset)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TButton_Send_Offset = ttk.Button(self.TLabelframe1)
        self.TButton_Send_Offset.place(relx=0.727, rely=0.435, height=29
                , width=48, bordermode='ignore')
        self.TButton_Send_Offset.configure(command=befehle_gui_support.btn_send_nullpunkt_offset)
        self.TButton_Send_Offset.configure(takefocus="")
        self.TButton_Send_Offset.configure(text='''Send''')

        self.TLabel2 = ttk.Label(self.TLabelframe1)
        self.TLabel2.place(relx=0.045, rely=0.435, height=23, width=67
                , bordermode='ignore')
        self.TLabel2.configure(background="#ffffff")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Nullpunkt:''')

        self.TLabel2_15 = ttk.Label(self.TLabelframe1)
        self.TLabel2_15.place(relx=0.045, rely=0.174, height=23, width=67
                , bordermode='ignore')
        self.TLabel2_15.configure(background="#ffffff")
        self.TLabel2_15.configure(foreground="#000000")
        self.TLabel2_15.configure(font="TkDefaultFont")
        self.TLabel2_15.configure(relief="flat")
        self.TLabel2_15.configure(text='''Sollwert:''')

        self.TEntry1_1 = ttk.Entry(self.TLabelframe1)
        self.TEntry1_1.place(relx=0.364, rely=0.174, relheight=0.217
                , relwidth=0.3, bordermode='ignore')
        self.TEntry1_1.configure(textvariable=befehle_gui_support.sollwert)
        self.TEntry1_1.configure(takefocus="")
        self.TEntry1_1.configure(cursor="ibeam")

        self.TButton_Send_Offset_16 = ttk.Button(self.TLabelframe1)
        self.TButton_Send_Offset_16.place(relx=0.727, rely=0.174, height=29
                , width=48, bordermode='ignore')
        self.TButton_Send_Offset_16.configure(command=befehle_gui_support.btn_send_sollwert)
        self.TButton_Send_Offset_16.configure(takefocus="")
        self.TButton_Send_Offset_16.configure(text='''Send''')

        self.TLabel2_4 = ttk.Label(self.TLabelframe1)
        self.TLabel2_4.place(relx=0.045, rely=0.696, height=23, width=67
                , bordermode='ignore')
        self.TLabel2_4.configure(background="#ffffff")
        self.TLabel2_4.configure(foreground="#000000")
        self.TLabel2_4.configure(font="TkDefaultFont")
        self.TLabel2_4.configure(relief="flat")
        self.TLabel2_4.configure(text='''Bias:''')

        self.TEntry1_5 = ttk.Entry(self.TLabelframe1)
        self.TEntry1_5.place(relx=0.364, rely=0.696, relheight=0.217
                , relwidth=0.3, bordermode='ignore')
        self.TEntry1_5.configure(textvariable=befehle_gui_support.bias)
        self.TEntry1_5.configure(takefocus="")
        self.TEntry1_5.configure(cursor="ibeam")

        self.TButton_Send_Offset_6 = ttk.Button(self.TLabelframe1)
        self.TButton_Send_Offset_6.place(relx=0.727, rely=0.696, height=29
                , width=48, bordermode='ignore')
        self.TButton_Send_Offset_6.configure(command=befehle_gui_support.btn_send_bias)
        self.TButton_Send_Offset_6.configure(takefocus="")
        self.TButton_Send_Offset_6.configure(text='''Send''')

        self.TLabelframe2 = ttk.Labelframe(top)
        self.TLabelframe2.place(relx=0.024, rely=0.369, relheight=0.526
                , relwidth=0.267)
        self.TLabelframe2.configure(relief='')
        self.TLabelframe2.configure(text='''PID''')

        self.TLabel1 = ttk.Label(self.TLabelframe2)
        self.TLabel1.place(relx=0.045, rely=0.162, height=23, width=15
                , bordermode='ignore')
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''P:''')

        self.TLabel1_1 = ttk.Label(self.TLabelframe2)
        self.TLabel1_1.place(relx=0.045, rely=0.324, height=23, width=15
                , bordermode='ignore')
        self.TLabel1_1.configure(background="#ffffff")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font="TkDefaultFont")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(text='''I:''')

        self.TLabel1_2 = ttk.Label(self.TLabelframe2)
        self.TLabel1_2.place(relx=0.045, rely=0.486, height=23, width=25
                , bordermode='ignore')
        self.TLabel1_2.configure(background="#ffffff")
        self.TLabel1_2.configure(foreground="#000000")
        self.TLabel1_2.configure(font="TkDefaultFont")
        self.TLabel1_2.configure(relief="flat")
        self.TLabel1_2.configure(text='''D:''')

        self.TEntry_Kp = ttk.Entry(self.TLabelframe2)
        self.TEntry_Kp.place(relx=0.182, rely=0.162, relheight=0.135
                , relwidth=0.573, bordermode='ignore')
        self.TEntry_Kp.configure(textvariable=befehle_gui_support.kp)
        self.TEntry_Kp.configure(takefocus="")
        self.TEntry_Kp.configure(cursor="fleur")

        self.TEntry_Ki = ttk.Entry(self.TLabelframe2)
        self.TEntry_Ki.place(relx=0.182, rely=0.324, relheight=0.135
                , relwidth=0.573, bordermode='ignore')
        self.TEntry_Ki.configure(textvariable=befehle_gui_support.ki)
        self.TEntry_Ki.configure(takefocus="")
        self.TEntry_Ki.configure(cursor="ibeam")

        self.TEntry_Kd = ttk.Entry(self.TLabelframe2)
        self.TEntry_Kd.place(relx=0.182, rely=0.486, relheight=0.135
                , relwidth=0.573, bordermode='ignore')
        self.TEntry_Kd.configure(textvariable=befehle_gui_support.kd)
        self.TEntry_Kd.configure(takefocus="")
        self.TEntry_Kd.configure(cursor="ibeam")

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(self.TLabelframe2)
        self.TCheckbutton1.place(relx=0.045, rely=0.649, relwidth=0.236
                , relheight=0.0, height=25, bordermode='ignore')
        self.TCheckbutton1.configure(variable=befehle_gui_support.PoM)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''PoM''')

        self.TButtonSend_PID = ttk.Button(self.TLabelframe2)
        self.TButtonSend_PID.place(relx=0.091, rely=0.811, height=29, width=178
                , bordermode='ignore')
        self.TButtonSend_PID.configure(command=befehle_gui_support.btn_send_pid_values)
        self.TButtonSend_PID.configure(takefocus="")
        self.TButtonSend_PID.configure(text='''Send''')

        self.TLabelframe3 = ttk.Labelframe(top)
        self.TLabelframe3.place(relx=0.316, rely=0.028, relheight=0.611
                , relwidth=0.303)
        self.TLabelframe3.configure(relief='')
        self.TLabelframe3.configure(text='''Overwrite''')

        self.TLabel3 = ttk.Label(self.TLabelframe3)
        self.TLabel3.place(relx=0.04, rely=0.093, height=23, width=46
                , bordermode='ignore')
        self.TLabel3.configure(background="#ffffff")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''Zone0:''')

        self.TLabel3_6 = ttk.Label(self.TLabelframe3)
        self.TLabel3_6.place(relx=0.04, rely=0.233, height=23, width=46
                , bordermode='ignore')
        self.TLabel3_6.configure(background="#ffffff")
        self.TLabel3_6.configure(foreground="#000000")
        self.TLabel3_6.configure(font="TkDefaultFont")
        self.TLabel3_6.configure(relief="flat")
        self.TLabel3_6.configure(text='''Zone1:''')

        self.TLabel3_7 = ttk.Label(self.TLabelframe3)
        self.TLabel3_7.place(relx=0.04, rely=0.372, height=23, width=46
                , bordermode='ignore')
        self.TLabel3_7.configure(background="#ffffff")
        self.TLabel3_7.configure(foreground="#000000")
        self.TLabel3_7.configure(font="TkDefaultFont")
        self.TLabel3_7.configure(relief="flat")
        self.TLabel3_7.configure(text='''Zone2:''')

        self.TLabel3_8 = ttk.Label(self.TLabelframe3)
        self.TLabel3_8.place(relx=0.04, rely=0.512, height=23, width=46
                , bordermode='ignore')
        self.TLabel3_8.configure(background="#ffffff")
        self.TLabel3_8.configure(foreground="#000000")
        self.TLabel3_8.configure(font="TkDefaultFont")
        self.TLabel3_8.configure(relief="flat")
        self.TLabel3_8.configure(text='''Zone3:''')

        self.TEntry_Ovewrite1 = ttk.Entry(self.TLabelframe3)
        self.TEntry_Ovewrite1.place(relx=0.28, rely=0.093, relheight=0.116
                , relwidth=0.664, bordermode='ignore')
        self.TEntry_Ovewrite1.configure(textvariable=befehle_gui_support.overwrite0)
        self.TEntry_Ovewrite1.configure(takefocus="")
        self.TEntry_Ovewrite1.configure(cursor="ibeam")

        self.TEntry_Ovewrite2 = ttk.Entry(self.TLabelframe3)
        self.TEntry_Ovewrite2.place(relx=0.28, rely=0.233, relheight=0.116
                , relwidth=0.664, bordermode='ignore')
        self.TEntry_Ovewrite2.configure(textvariable=befehle_gui_support.overwrite1)
        self.TEntry_Ovewrite2.configure(takefocus="")
        self.TEntry_Ovewrite2.configure(cursor="fleur")

        self.TEntry_Ovewrite3 = ttk.Entry(self.TLabelframe3)
        self.TEntry_Ovewrite3.place(relx=0.28, rely=0.372, relheight=0.116
                , relwidth=0.664, bordermode='ignore')
        self.TEntry_Ovewrite3.configure(textvariable=befehle_gui_support.overwrite2)
        self.TEntry_Ovewrite3.configure(takefocus="")
        self.TEntry_Ovewrite3.configure(cursor="ibeam")

        self.TEntry_Ovewrite4 = ttk.Entry(self.TLabelframe3)
        self.TEntry_Ovewrite4.place(relx=0.28, rely=0.512, relheight=0.116
                , relwidth=0.664, bordermode='ignore')
        self.TEntry_Ovewrite4.configure(textvariable=befehle_gui_support.overwrite3)
        self.TEntry_Ovewrite4.configure(takefocus="")
        self.TEntry_Ovewrite4.configure(cursor="ibeam")

        self.TButton_overwrite = ttk.Button(self.TLabelframe3)
        self.TButton_overwrite.place(relx=0.08, rely=0.791, height=29, width=98
                , bordermode='ignore')
        self.TButton_overwrite.configure(command=befehle_gui_support.btn_send_overwrite)
        self.TButton_overwrite.configure(takefocus="")
        self.TButton_overwrite.configure(text='''overwrite''')

        self.TButton_regelung = ttk.Button(self.TLabelframe3)
        self.TButton_regelung.place(relx=0.52, rely=0.791, height=29, width=98
                , bordermode='ignore')
        self.TButton_regelung.configure(command=befehle_gui_support.btn_set_automatic)
        self.TButton_regelung.configure(takefocus="")
        self.TButton_regelung.configure(text='''automatic''')

        self.TLabel3_2 = ttk.Label(self.TLabelframe3)
        self.TLabel3_2.place(relx=0.04, rely=0.651, height=23, width=46
                , bordermode='ignore')
        self.TLabel3_2.configure(background="#ffffff")
        self.TLabel3_2.configure(foreground="#000000")
        self.TLabel3_2.configure(font="TkDefaultFont")
        self.TLabel3_2.configure(relief="flat")
        self.TLabel3_2.configure(text='''GND:''')

        self.TEntry_OvewriteGND = ttk.Entry(self.TLabelframe3)
        self.TEntry_OvewriteGND.place(relx=0.28, rely=0.651, relheight=0.116
                , relwidth=0.664, bordermode='ignore')
        self.TEntry_OvewriteGND.configure(textvariable=befehle_gui_support.overwrite_gnd)
        self.TEntry_OvewriteGND.configure(takefocus="")
        self.TEntry_OvewriteGND.configure(cursor="ibeam")

        self.sonstiges = ttk.Labelframe(top)
        self.sonstiges.place(relx=0.316, rely=0.653, relheight=0.241
                , relwidth=0.303)
        self.sonstiges.configure(relief='')
        self.sonstiges.configure(text='''sonstiges''')

        self.TButton1 = ttk.Button(self.sonstiges)
        self.TButton1.place(relx=0.04, rely=0.235, height=29, width=58
                , bordermode='ignore')
        self.TButton1.configure(command=befehle_gui_support.btn_send_off)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''aus''')

        self.TButton1_13 = ttk.Button(self.sonstiges)
        self.TButton1_13.place(relx=0.28, rely=0.235, height=29, width=88
                , bordermode='ignore')
        self.TButton1_13.configure(command=befehle_gui_support.btn_send_offsweep)
        self.TButton1_13.configure(takefocus="")
        self.TButton1_13.configure(text='''aus(sweep)''')

        self.TButton1_14 = ttk.Button(self.sonstiges)
        self.TButton1_14.place(relx=0.04, rely=0.588, height=29, width=58
                , bordermode='ignore')
        self.TButton1_14.configure(command=befehle_gui_support.btn_send_fullon)
        self.TButton1_14.configure(takefocus="")
        self.TButton1_14.configure(text='''full_on''')

        self.TLabelframe2_1 = ttk.Labelframe(top)
        self.TLabelframe2_1.place(relx=0.631, rely=0.028, relheight=0.44
                , relwidth=0.267)
        self.TLabelframe2_1.configure(relief='')
        self.TLabelframe2_1.configure(text='''sweep''')

        self.TLabel1_2 = ttk.Label(self.TLabelframe2_1)
        self.TLabel1_2.place(relx=0.045, rely=0.194, height=23, width=39
                , bordermode='ignore')
        self.TLabel1_2.configure(background="#ffffff")
        self.TLabel1_2.configure(foreground="#000000")
        self.TLabel1_2.configure(font="TkDefaultFont")
        self.TLabel1_2.configure(relief="flat")
        self.TLabel1_2.configure(text='''delay:''')

        self.TLabel1_2 = ttk.Label(self.TLabelframe2_1)
        self.TLabel1_2.place(relx=0.045, rely=0.387, height=23, width=45
                , bordermode='ignore')
        self.TLabel1_2.configure(background="#ffffff")
        self.TLabel1_2.configure(foreground="#000000")
        self.TLabel1_2.configure(font="TkDefaultFont")
        self.TLabel1_2.configure(relief="flat")
        self.TLabel1_2.configure(text='''dec:''')

        self.TLabel1_3 = ttk.Label(self.TLabelframe2_1)
        self.TLabel1_3.place(relx=0.045, rely=0.581, height=23, width=45
                , bordermode='ignore')
        self.TLabel1_3.configure(background="#ffffff")
        self.TLabel1_3.configure(foreground="#000000")
        self.TLabel1_3.configure(font="TkDefaultFont")
        self.TLabel1_3.configure(relief="flat")
        self.TLabel1_3.configure(text='''start:''')

        self.TEntry_Kp_4 = ttk.Entry(self.TLabelframe2_1)
        self.TEntry_Kp_4.place(relx=0.273, rely=0.194, relheight=0.161
                , relwidth=0.573, bordermode='ignore')
        self.TEntry_Kp_4.configure(textvariable=befehle_gui_support.sweep_delay)
        self.TEntry_Kp_4.configure(takefocus="")
        self.TEntry_Kp_4.configure(cursor="fleur")

        self.TEntry_Ki_5 = ttk.Entry(self.TLabelframe2_1)
        self.TEntry_Ki_5.place(relx=0.273, rely=0.387, relheight=0.161
                , relwidth=0.573, bordermode='ignore')
        self.TEntry_Ki_5.configure(textvariable=befehle_gui_support.sweep_dec)
        self.TEntry_Ki_5.configure(takefocus="")
        self.TEntry_Ki_5.configure(cursor="ibeam")

        self.TEntry_Kd_6 = ttk.Entry(self.TLabelframe2_1)
        self.TEntry_Kd_6.place(relx=0.273, rely=0.581, relheight=0.161
                , relwidth=0.573, bordermode='ignore')
        self.TEntry_Kd_6.configure(textvariable=befehle_gui_support.sweep_start)
        self.TEntry_Kd_6.configure(takefocus="")
        self.TEntry_Kd_6.configure(cursor="ibeam")

        self.TButtonSend_sweep = ttk.Button(self.TLabelframe2_1)
        self.TButtonSend_sweep.place(relx=0.091, rely=0.774, height=29, width=178
                , bordermode='ignore')
        self.TButtonSend_sweep.configure(command=befehle_gui_support.btn_send_sweep_values)
        self.TButtonSend_sweep.configure(takefocus="")
        self.TButtonSend_sweep.configure(text='''Send''')

if __name__ == '__main__':
    vp_start_gui()





