import serial, sys
import matplotlib.pyplot as plt
from datetime import date
import time

x=range(0, 100, 1)
data=[0]*100
ser = serial.Serial(sys.argv[1],9600)

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="S_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

while True:
  ttime=time.time()-start
  if ttime<0.001:
    ttime=0.0
  try:
    line = ser.readline()
    line2=float(line.strip().decode('utf-8'))
    data.pop(-1)
    data.insert(0,line2)
    plt.clf()
    plt.ylim([0,20.0])
    plt.plot(x,data)
    plt.pause(0.1)
    st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
    ss=str(time.time()-int(time.time()))
    rttime=round(ttime,2)
    strg=str(st+ss[1:5])+","+str(rttime)+","+str(line2)+"\n"
    f.write(strg)
    print(strg)
  except KeyboardInterrupt:
    print ('exiting')
    f.close()
    break
exit()
