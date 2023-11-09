# PySerial-MCU-Communicator
This is designed to facilitate real-time communication between a computer and a microcontroller using the PySerial library. 

It is currently only operational on the ESP32 however currently working on HAL UART commands for ARM mBed dev.

### Running the communicator:
1)  ```
    pip install pyserial
    ```
2)  Be sure to update the COM port in python.
    ``
    port = serial.Serial("COM5", baudrate=115200, timeout=1)
    ``
3) Open a terminal or command prompt and navigate to the project directory.
4) Run the Python script by executing the following command: ``python pyserial_mcu_communicator.py
``
