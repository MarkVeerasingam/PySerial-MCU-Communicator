import serial
import time
import random

MAX_BUFF_LEN = 255

port = serial.Serial("COM5", baudrate=115200, timeout=1)

def read_ser(num_char = 1):
    data = port.read(num_char)
    return data.decode()

def write_ser(cmd):
    cmd = cmd + '\n'
    port.write(cmd.encode())

while(True):
    # Generate random data and send in real time
    random_data = str(random.randint(0,100))  

    # Send the random data
    write_ser(random_data)

    # Read and print any incoming data
    string = read_ser(MAX_BUFF_LEN)
    print(string)

    # Sleep for 100  ms 
    time.sleep(.1) 