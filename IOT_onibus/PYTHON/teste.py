import serial
arduino = serial.Serial('COM4', 9600)
l = []

for i in range(5):
    l.append(str(arduino.readline()))
    
for i in l:
    if i[2] == 'b':
        print((i[2:14]))
    if i[2] == 'a':
        print((i[2:14]))
 
print("===================")
print(l[0])
print("===================")
print(l[1])
#print("===================")
#print(l[2])
#print("===================")
#print(l[3])
#print("===================")
arduino.close( )