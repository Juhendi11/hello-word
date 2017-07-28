"""
 buat grafik 3X3, accelerometer secara real time
 time format sampai ke detik
 time serias,
 membuat data series 1 herz, sampai 10 hz
 """

from datetime import datetime
import serial
import matplotlib.pyplot as plt
from drawnow import *
import time

#data dari sensor

datax = []
datay = []
dataz = []
waktu = []
plt.ion()

ser = serial.Serial('/dev/ttyUSB0',baudrate=115200, timeout=1)

def buatgrafik():
	plt.title("grafik data accelero realtime")
	#plt.grid(True)
	plt.ylabel("data")
	plt.xlabel('jumlah data')
	plt.plot(datax,  '-', label='sumbu x')
	plt.plot(datay, '-', label='sumbu y')
	plt.plot(dataz, '-', label='sumbu z')
	plt.legend(loc="upper left")
	plt.gcf().autofmt_xdate()
	
	#masalah kecepatan plot????
	
while True:
	while (ser.inWaiting()==0):
		pass 
	timestamp = str(time.strftime("%d %Y %H:%M:%S", time.gmtime()))
	datastring = ser.readline() #membaca data perbaris
	with  open('outpADXL.txt1', 'a') as pyfile:
		pyfile.write(datastring+ '    ' + timestamp )
	dataArray =  datastring.split(',') #memecah string menjadi list
	x = float( dataArray[0])
	y = float( dataArray[1])
	z = float( dataArray[2])
	#menambah data dari variabel x ,y z ke variabel datax, datay, dataz
	datax.append(x) 
	datay.append(y)
	dataz.append(z)
	waktu.append(timestamp)

	drawnow(buatgrafik)                       #Call drawnow to update our live graph
	plt.pause(0.0000001)
	
	
	

ser.close()
