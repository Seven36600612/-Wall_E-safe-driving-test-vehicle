# coding:utf-8
import RPi.GPIO as GPIO
import signal

from mfrc522 import MFRC522

continue_reading = True


# 捕获SIGINT以便在脚本中止时进行清理
def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
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
        print ("Card detected")

    # 获取卡的UID
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    flag = 1

    # 如果我们有UID，继续
    if status == MIFAREReader.MI_OK:

        # 打印UID
        print ("Card read UID: %s,%s,%s,%s %s" % (uid[0], uid[1], uid[2], uid[3], uid[4]))

        # 这是身份验证的默认密钥
        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

        # 选择扫描的标签
        MIFAREReader.MFRC522_SelectTag(uid)

        # 认证
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # 检查是否已验证
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
            flag = 0
        else:
            # 身份验证错误
            print ("Authentication error")