import serial
import time

ser = serial.Serial(
    port='COM1',\
    baudrate=57600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
ser.reset_input_buffer()
ser.reset_output_buffer()
   
print("connected to: " + ser.portstr)
c=5
d=5
e=5
f=5
g=5
h=5
x=""
while True:
    serialrad=ser.readline()
    serialrads=serialrad.split()
    #serialrads=serialrad.lstrip()
    for line in serialrads:
        line=line.decode('utf-8',"ignore")
        #print(" {0}".format(line.decode()))
        print (x.join(line))
        if line=='autoboo':
            print ("*********Got the Message:")
            c=1
        if (line=="t:") and c==1:
            print ("*********Got AUTOMESSAGE:")
            d=1
        if (line=="3") and d==1:
            c=0
            d=0
            print("3 level passes")
            sen='a'
            sen=sen.encode()
            ser.write(sen)
        if (line=="xxxxxxx-xxxxx>"):
            print(" got the  message")
            sen='run diag\r'
            print (sen)
            sen=sen.encode()
            #print (sen)
            ser.write(sen)
        #print (line)
        if (line=="mode"):
            e=1
        if (line==">>") and e==1:
            e=0
            sen='xxxxxxx\r'
            sen=sen.encode()
            #print (sen)
            ser.write(sen)
        if (line=="FAILED"):
            print("*******CARD TEST FAILED****")
            ser.close()
            exit()
        if (line=="xxxxxxxxxxxxxxxxx"):
            f=1
        if (line=="SUCCESS") and f==1:
            f=0
            print("xxxxxx PASSED")
            sen='menu\r'
            print (sen)
            sen=sen.encode()
            ser.write(sen)
            g=1
        if (line=="choice>") and g==1:
            g=0
            sen='11\r'
            print (sen)
            sen=sen.encode()
            ser.write(sen)
            time.sleep(1)
            sen='1\r'
            print (sen)
            sen=sen.encode()
            ser.write(sen)
            time.sleep(1)
            sen='5\r'
            print (sen)
            sen=sen.encode()
            ser.write(sen)
        
        
ser.close()
