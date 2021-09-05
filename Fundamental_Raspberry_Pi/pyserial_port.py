import serial.tools.list_ports
 
plist = list(serial.tools.list_ports.comports())
 
if len(plist) <= 0:
    print("no serial port")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 9600, timeout=60)
    print("find serial port named: ", serialFd.name)
