import RPi.GPIO as GPIO
from mfrc522 import MFRC522
import signal

continue_reading = True


# 捕获SIGINT以便在脚本中止时进行清理
def end_read(signal, frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


# 连接信号
signal.signal(signal.SIGINT, end_read)

# 创建MFRC522类的对象
MIFAREReader = MFRC522()

# 这个循环一直在检查芯片。如果有一个在附近，它将获得UID并进行身份验证
while continue_reading:

    # 扫描卡片
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # 如果找到一张卡
    if status == MIFAREReader.MI_OK:
        print("Card detected")

    # 获取卡的UID
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # 如果我们有UID，继续
    if status == MIFAREReader.MI_OK:

        # 打印UID
        print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))

        # 这是身份验证的默认密钥
        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

        # 选择扫描的标签
        MIFAREReader.MFRC522_SelectTag(uid)

        # 认证
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        print("\n")

        # 检查是否已验证
        if status == MIFAREReader.MI_OK:

            # 要写入的数据的变量
            data = []

            # 用0xFF填充数据
            for x in range(0, 16):
                data.append(0xFF)

            # 第8区是这样的：
            print("Sector 8 looked like this:")

            # 读取块8
            MIFAREReader.MFRC522_Read(8)
            print("\n")

            # 扇区8现在将填充0xFF：
            print("Sector 8 will now be filled with 0xFF:")

            # 写入数据
            MIFAREReader.MFRC522_Write(8, data)
            print("\n")

            # 现在看起来像这样：
            print("It now looks like this:")

            # 看看是不是写的
            MIFAREReader.MFRC522_Read(8)
            print("\n")

            data = []
            # 用0x00填充数据
            for x in range(0, 16):
                data.append(0x00)

            # 现在我们用0x00填充它：
            print("Now we fill it with 0x00:")
            MIFAREReader.MFRC522_Write(8, data)
            print("\n")

            # 它现在是空的：
            print("It is now empty:")

            # 看看是不是写的
            MIFAREReader.MFRC522_Read(8)
            print("\n")

            # 住手
            MIFAREReader.MFRC522_StopCrypto1()

            # 一定要停止读卡
            continue_reading = False
        else:

            # 身份验证错误
            print("Authentication error")
