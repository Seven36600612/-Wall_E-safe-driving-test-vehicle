import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
def setup(Addr):
    global address
    address = Addr

def read(chn): #channel
    if chn == 0:
        bus.write_byte(address,0x40)
    if chn == 1:
        bus.write_byte(address,0x41)
    if chn == 2:
        bus.write_byte(address,0x42)
    if chn == 3:
        bus.write_byte(address,0x43)
    bus.read_byte(address) # dummy read to start conversion
    return bus.read_byte(address)

def write(val):
    temp = val # move string value to temp
    temp = int(temp) # change string to integer
    # print temp to see on terminal else comment out
    bus.write_byte_data(address, 0x40, temp)

if __name__ == "__main__":
    setup(0x48)
    while True:
        print  ('AIN0 = '), read(0)
        print  ('AIN1 = '), read(1)
        print  ('AIN2 = '), read(2)
        tmp = read(0)
        tmp = tmp*(255-125)/255+125 # LED won't light up below 125, so convert '0-255' to '125-255'
        write(tmp)
        time.sleep(0.3)
