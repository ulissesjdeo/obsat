# https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi

from time import sleep
import smbus

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47


def data():
    def MPU_Init():
        bus.write_byte_data(deviceAddress, SMPLRT_DIV, 7)
        bus.write_byte_data(deviceAddress, PWR_MGMT_1, 1)
        bus.write_byte_data(deviceAddress, CONFIG, 0)
        bus.write_byte_data(deviceAddress, GYRO_CONFIG, 24)
        bus.write_byte_data(deviceAddress, INT_ENABLE, 1)

    def read_raw_data(addr):
        high = bus.read_byte_data(deviceAddress, addr)
        low = bus.read_byte_data(deviceAddress, addr + 1)
        value = ((high << 8) | low)
        if value > 32768:
            value = value - 65536
        return value

    bus = smbus.SMBus(1)
    deviceAddress = 0x68
    MPU_Init()

    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
    Ax = acc_x / 16384.0
    Ay = acc_y / 16384.0
    Az = acc_z / 16384.0
    Gx = gyro_x / 131.0
    Gy = gyro_y / 131.0
    Gz = gyro_z / 131.0

    return {"g": [Gx, Gy, Gz], "a": [Ax, Ay, Az]}  # print("Gx=%.2f" % Gx, u'\u00b0' + "/s", "\tGy=%.2f" % Gy, u'\u00b0' + "/s", "\tGz=%.2f" % Gz, u'\u00b0' + "/s", "\tAx=%.2f g" % Ax, "\tAy=%.2f g" % Ay, "\tAz=%.2f g" % Az)
