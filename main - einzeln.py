#!/usr/bin/env python
import math
import sys
from threading import Thread
import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import struct
import copy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as Tk
from tkinter.ttk import Frame
import pandas as pd


class serialPlot:
    def __init__(self, serialPort='/dev/ttyUSB0', serialBaud=38400, plotLength=100, dataNumBytes=2, numPlots=1):
        self.port = serialPort
        self.baud = serialBaud
        self.plotMaxLength = plotLength
        self.dataNumBytes = dataNumBytes
        self.numPlots = numPlots
        self.rawData = bytearray(numPlots * dataNumBytes)
        self.dataType = None
        if dataNumBytes == 2:
            self.dataType = 'h'     # 2 byte integer
        elif dataNumBytes == 4:
            self.dataType = 'f'     # 4 byte float
        self.data = []
        for i in range(numPlots):   # give an array for each type of data and store them in a list
            self.data.append(collections.deque([0] * plotLength, maxlen=plotLength))
        self.isRun = True
        self.isReceiving = False
        self.thread = None
        self.plotTimer = 0
        self.previousTimer = 0
        # self.csvData = []

        print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        try:
            self.serialConnection = serial.Serial(serialPort, serialBaud, timeout=4)
            print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        except:
            print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')

    def readSerialStart(self):
        if self.thread == None:
            self.thread = Thread(target=self.backgroundThread)
            self.thread.start()
            # Block till we start receiving values
            while self.isReceiving != True:
                time.sleep(0.1)

    def getSerialData(self, frame, lines, lineValueText, lineLabel, timeText):
        currentTimer = time.perf_counter()
        self.plotTimer = int((currentTimer - self.previousTimer) * 1000)     # the first reading will be erroneous
        self.previousTimer = currentTimer
        timeText.set_text('Plot Interval = ' + str(self.plotTimer) + 'ms')
        privateData = copy.deepcopy(self.rawData[:])    # so that the 3 values in our plots will be synchronized to the same sample time
        for i in range(self.numPlots):
            data = privateData[(i*self.dataNumBytes):(self.dataNumBytes + i*self.dataNumBytes)]
            value,  = struct.unpack(self.dataType, data)
            value = round(value,5)
            self.data[i].append(value)    # we get the latest data point and append it to our array
            lines[i].set_data(range(self.plotMaxLength), self.data[i])
            lineValueText[i].set_text('[' + lineLabel[i] + '] = ' + str(value))
        # self.csvData.append([self.data[0][-1], self.data[1][-1], self.data[2][-1]])

    def getSerialData2(self, frame, lines, lineValueText, lineLabel, timeText):
        currentTimer = time.perf_counter()
        plotTimer = int((currentTimer - self.previousTimer) * 1000)     # the first reading will be erroneous
        self.previousTimer = currentTimer
        timeText.set_text('Plot Interval = ' + str(plotTimer) + 'ms')
        privateData = copy.deepcopy(self.rawData[:])    # so that the 3 values in our plots will be synchronized to the same sample time
        for i in range(self.numPlots):
            data = privateData[(i*self.dataNumBytes):(self.dataNumBytes + i*self.dataNumBytes)]
            value,  = struct.unpack(self.dataType, data)
            value = round(value,5)
            self.data[i].append(value)    # we get the latest data point and append it to our array
            lines[i].set_data(range(self.plotMaxLength), self.data[i])
            lineValueText[i].set_text('[' + lineLabel[i] + '] = ' + str(value))
        # self.csvData.append([self.data[0][-1], self.data[1][-1], self.data[2][-1]])


    def backgroundThread(self):    # retrieve data
        time.sleep(1.0)  # give some buffer time for retrieving data
        self.serialConnection.reset_input_buffer()
        while (self.isRun):
            self.serialConnection.readinto(self.rawData)
            self.isReceiving = True
            #print(self.rawData)

    def sendSerialData(self, data):
        self.serialConnection.write(data.encode('utf-8'))

    def close(self):
        self.isRun = False
        self.thread.join()
        self.serialConnection.close()
        print('Disconnected...')
        # df = pd.DataFrame(self.csvData)
        # df.to_csv('/home/rikisenia/Desktop/data.csv')


class Window(Frame):
    def __init__(self, figure1,figure2, master, SerialReference):
        Frame.__init__(self, master)
        self.entry = None
        self.setPoint = None
        self.master = master        # a reference to the master window
        self.serialReference = SerialReference      # keep a reference to our serial connection so that we can use it for bi-directional communicate from this class
        self.initWindow(figure1,figure2)     # initialize the window with our settings
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.serialReference.close();
        sys.exit()
    def initWindow(self, figure1,figure2):
        self.master.title("Leviosa")
        canvas1 = FigureCanvasTkAgg(figure1, master=self.master)
        canvas2 = FigureCanvasTkAgg(figure2, master=self.master)
        toolbar1 = NavigationToolbar2Tk(canvas1, self.master)
        toolbar2 = NavigationToolbar2Tk(canvas2, self.master)
        frame2 = Frame(self.master)
        frame2.pack(side=Tk.BOTTOM)

        canvas1.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        canvas2.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        # create a new frame to place our widgets


        # create out widgets in the frame2
        lbl1 = Tk.Label(frame2, text="Offset")
        lbl1.pack(padx=5, pady=5)
        self.entry = Tk.Entry(frame2)
        self.entry.insert(0, '1.0')     # (index, string)
        self.entry.pack(padx=5)
        SendButton = Tk.Button(frame2, text='Send', command=self.sendFactorToMCU)
        SendButton.pack(padx=5)

    def sendFactorToMCU(self):
        self.serialReference.sendSerialData(self.entry.get() + '%')     # '%' is our ending marker

def main():
    portName = 'COM6'
    #portName = '/dev/ttyUSB0'
    baudRate = 38400
    maxPlotLength = 100     # number of points in x-axis of real time plot
    dataNumBytes = 4        # number of bytes of 1 data point
    numPlots = 4            # number of plots in 1 graph
    s = serialPlot(portName, baudRate, maxPlotLength, dataNumBytes, numPlots)   # initializes all required variables
    s.readSerialStart()                                               # starts background thread

    # plotting starts below
    pltInterval = 50    # Period at which the plot animation updates [ms]
    xmin = 0
    xmax = maxPlotLength
    ymin = -(1)
    ymax = 1
    fig1 = plt.figure(figsize=(5, 8))
    ax1 = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax1.set_title('Abstandsabweichung')
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Abstand")

    fig2 = plt.figure(figsize=(5, 8))
    ax2 = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax2.set_title('Reglerausgang')
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Spannung")

    # put our plot onto Tkinter's GUI
    root = Tk.Tk()
    app = Window(fig1,fig2, root, s)

    lineLabel = ['1', '2', '3','4']
    style = ['r-', 'c-', 'b-','y']  # linestyles for the different plots
    timeText = ax1.text(0.50, 0.95, '', transform=ax1.transAxes)
    lines = []
    lineValueText = []
    for i in range(numPlots):
        lines.append(ax1.plot([], [], style[i], label=lineLabel[i])[0])
        lineValueText.append(ax1.text(0.50, 0.90-i*0.05, '', transform=ax1.transAxes))

    lines2 = []
    lineValueText2 = []
    for i in range(numPlots):
        lines2.append(ax2.plot([], [], style[i], label=lineLabel[i])[0])
        lineValueText2.append(ax2.text(0.50, 0.90 - i * 0.05, '', transform=ax2.transAxes))

    anim = animation.FuncAnimation(fig1, s.getSerialData, fargs=(lines, lineValueText, lineLabel, timeText), interval=pltInterval)    # fargs has to be a tuple
    anim2 = animation.FuncAnimation(fig2, s.getSerialData2, fargs=(lines2, lineValueText2, lineLabel, timeText),
                                   interval=pltInterval)  # fargs has to be a tuple

    plt.legend(loc="upper left")
    root.mainloop()   # use this instead of plt.show() since we are encapsulating everything in Tkinter



if __name__ == '__main__':
    main()
