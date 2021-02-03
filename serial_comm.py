import serial
import time
import json

def check_port():
    port_list = []
    from serial.tools import list_ports
    ports = list_ports.comports()  # Outputs list of available serial ports
    for port in ports :
        port_list.append(port.name)
    return port_list

class connect():
    port =  check_port()
    port = port[0]
    ser = serial.Serial(port,115200,timeout=2)

def send_comm(data):
    try:
        serComm = json.dumps({"comm":data})
        sd = bytes(serComm,'utf-8')
        connect.ser.write(sd)
        print("Command send : ",sd)
    except Exception as e:
        #print('Serial side: ',e)
        pass

def read():
    try:
        line = connect.ser.readline().decode('utf-8').rstrip()
        #input_serial = json.loads(line)
        return line
    except Exception as e:
        pass
try:
    if check_port() != []:
        print("Found device : ",check_port())
    else:
        print("No device ! ")

except  Exception as e:
    pass