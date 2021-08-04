# This is the python file for the custom MKR1000 part for the DonkeyCar. You need to edit your MKR1000's serial port in the Raspberry Pi, and place it in the mycar directory.

import serial
import time

class MKR1000Serial:
    def update(self):
        print('Starting MKR1000 serial connection...')
    def run_threaded(self):
        ser = serial.Serial('/dev/ttyACM0', 9600)
        ser.write(b"1")
        time.sleep(0.0625)
        if(ser.in_waiting >0):
            line = ser.readline()
            command = line.decode("utf-8")
            letterDetected,bluetoothConnected = command.split(':')
            print(letterDetected,",",bluetoothConnected)
