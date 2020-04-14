import serial
global ser
ser = serial.Serial('/dev/ttyACM0',4800, 8, 'N', 1, timeout=1)
data = ser.readline()
print(data)
