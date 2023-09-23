# https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi

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
    def mpu_init():
        bus.write_byte_data(device_address, SMPLRT_DIV, 7)
        bus.write_byte_data(device_address, PWR_MGMT_1, 1)
        bus.write_byte_data(device_address, CONFIG, 0)
        bus.write_byte_data(device_address, GYRO_CONFIG, 24)
        bus.write_byte_data(device_address, INT_ENABLE, 1)

    def read_raw_data(addr):
        high = bus.read_byte_data(device_address, addr)
        low = bus.read_byte_data(device_address, addr + 1)
        value = ((high << 8) | low)
        if value > 32768:
            value = value - 65536
        return value

    bus = smbus.SMBus(1)
    device_address = 0x68
    mpu_init()

    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
    ax = acc_x / 16384.0
    ay = acc_y / 16384.0
    az = acc_z / 16384.0
    gx = gyro_x / 131.0
    gy = gyro_y / 131.0
    gz = gyro_z / 131.0

    return {"g": [gx, gy, gz], "a": [ax, ay, az]}  # print("gx=%.2f" % gx, u'\u00b0' + "/s", "\tgy=%.2f" % gy, u'\u00b0' + "/s", "\tgz=%.2f" % gz, u'\u00b0' + "/s", "\tax=%.2f g" % ax, "\tay=%.2f g" % ay, "\taz=%.2f g" % az)
