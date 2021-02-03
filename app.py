try:
   import serial_comm as ser
except  Exception as e:
    exit()


while True:
    try:
        value = ser.read()
        if value != "":
            print(value)
    except Exception as e:
        ser.connect()