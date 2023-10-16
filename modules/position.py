# https://docs.sunfounder.com/projects/sensorkit-v2-pi/en/latest/lesson_32.html

from smbus2 import SMBus

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
address = 0x68  # This is the address value read via the i2cdetect command


def read_byte(adr): return bus.read_byte_data(address, adr)


def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr + 1)
    val = (high << 8) + low
    return val


def read_word_2c(adr):
    val = read_word(adr)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val


bus = SMBus(1)
bus.write_byte_data(address, power_mgmt_1, 0)


def data():
    gx = read_word_2c(0x43)
    gy = read_word_2c(0x45)
    gz = read_word_2c(0x47)
    ax = read_word_2c(0x3b)
    ay = read_word_2c(0x3d)
    az = read_word_2c(0x3f)
    return {"g": [gx, gy, gz], "a": [ax, ay, az]}
