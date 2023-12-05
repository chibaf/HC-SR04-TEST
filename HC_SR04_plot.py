import serial, sys
import matplotlib.pyplot as plt

x=range(0, 100, 1)
data=[0]*100
ser = serial.Serial(sys.argv[1],9600)
while True:
  try:
    line = ser.readline()
    line2=float(line.strip().decode('utf-8'))
    data.pop(-1)
    data.insert(0,line2)
    plt.clf()
    plt.ylim([0,20.0])
    plt.plot(x,data)
    plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    break
exit()
