import serial


class SerialCommunication:
    def __init__(self):
        self.com = serial.Serial("COM3", 921600, write_timeout=10)

    def sending_data(self, command: str) -> None:
        self.com.write(command.encode('ascii'))
