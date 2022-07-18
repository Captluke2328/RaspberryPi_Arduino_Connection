"""
Author : Lukas Johnny
Date : 18/7/2022
Description : This script is used to establish the connection between RPI to Arduino using RX and TX
             Arduino : Tx --Connect -- Rpi : Rx
             Arduino : Rx --Connect -- Rpi : Tx

             Before running this code do ensure to:
             1. sudo raspi-config and enable SPI
             2. disable Serial login shell connection and enable Serial interface connection
             3. go to sudo vi /boot/config.txt -last line. Disable bluetooth using this command
             "dtoverlay=disable-bt"
             4. Reboot the Pi
             5. if ttyAMAO is not in dev, please enable_uart=1 in /boot/config too.
             6. ttyAMAO is serial protocol to connect PI and Arduino


"""
import serial
from time import sleep

class readdatafromArdtoRpi():
    def initConnection(self,portNo, baudRate):
        try:
            ser = serial.Serial(portNo, baudRate)
            print("Device Connected")
            return ser
        except:
            print("Not connected")

    def getData(self,ser):
        data = ser.readline()
        data = data.decode("utf-8")
        data = data.split("#")

        dataList = []
        [dataList.append(d) for d in data]
        return dataList[:-1]
    
if __name__ == "__main__":
    init = readdatafromArdtoRpi()
    ser = init.initConnection("/dev/ttyAMA0", 9600)

    while True:
        receivedata = init.getData(ser)
        print(receivedata)
