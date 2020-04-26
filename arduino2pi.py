import serial
import time
import matplotlib.pyplot as plot
starttime=time.time()
ser = serial.Serial('COM3', 9600)
line = ser.readline()
line = line.decode( 'utf-8' )
print(line)
x = []
y = []
exectime=0
while exectime<60:
    time.sleep(2)
    line = ser.readline()
    line=line.decode('utf-8')
    print(line)
    num1 = str(line[30])
    num2 = str(line[31])
    num3 = str(line[32])
    num4 = str(line[33])
    num5 = str(line[34])
    finalnum = num1+num2+num3+num4+num5
    print(time.asctime())
    print(finalnum)
    f= open("tempinfo.txt", "a")
    f.write(time.asctime())
    f.write(": ")
    f.write(finalnum)
    f.write("°C \n")
    f.close()
    y.append(finalnum)
    x.append(int(exectime))
    exectime=time.time()-starttime
    print(exectime, "Seconds")
plot.plot(x,y)
plot.ylabel('Temp (degrees celcius)')
plot.xlabel('Time elapsed (seconds)')
plot.gca().invert_yaxis()
plot.show()

