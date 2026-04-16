import serial
import threading

serialport = "/dev/cu.usbserial-110"

ser = serial.Serial(
    port=serialport,
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=0.1
)


def reader():
    while True:
        if ser.in_waiting:
            data = ser.read(ser.in_waiting)
            print(data.decode(errors="ignore"), end="")


threading.Thread(target=reader, daemon=True).start()


print("Connected. Type commands:")

while True:
    cmd = input("")
    ser.write((cmd + "\r\n").encode("ascii"))
