import serial
import time
import matplotlib.pyplot as plot
import matplotlib.animation as animation
maxtime = 10
interval = 2 #recommended to leave at 2

x=[]
y=[]
serconfig = serial.Serial('COM3', 9600)    
plt = plot.figure() 
graph = plt.add_subplot(1,1,1)
def graphdata(f):
    global x
    global y
    time.sleep(interval)
    line=serconfig.readline()
    line= line.decode('utf-8')
    line= float(line)
    print(line)
    y.append(line)
    x.append(time.asctime())
    x=x[-20:]
    y=y[-20:]
    graph.clear()
    graph.plot (x,y)
    plot.xticks(rotation=45, ha='right')
    plot.savefig('temp.png')
animated = animation.FuncAnimation(plt, graphdata, interval=100 )
plot.show()

