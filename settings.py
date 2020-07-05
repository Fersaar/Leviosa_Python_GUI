
#Serialconfig
portName = 'COM6'
# portName = '/dev/ttyUSB0'
baudRate = 38400
maxPlotLength = 100  # number of points in x-axis of real time plot
dataNumBytes = 4  # number of bytes of 1 data point
numPlots = 8  # number of datapoints

#Plotting
pltInterval = 1    # Period at which the plot animation updates [ms]
xmin = 0
xmax = maxPlotLength
y1_min = -(1000)
y1_max = 1000
y2_min = 0
y2_max = 65000