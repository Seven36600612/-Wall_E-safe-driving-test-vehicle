import RPi.GPIO as GPIO
import time

makerobo_TRIG = 13 #超声波距离传感器模块TRIG控制引脚
makerobo_ECHO = 15 #超声波距离传感器模块ECHO控制引脚
# 超声波距高传感器模块初始化工作
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD) #采用实际的物理引脚给 GPIO 口
    GPIO.setwarnings (False) #忽略 GPIO 口操作警告
    GPIO.setup(makerobo_TRIG, GPIO.OUT) #将引脚TRIG设置为输出模式
    GPIO.setup(makerobo_ECHO, GPIO.IN) #将引脚ECHO设置为输入模式
#超声波计算距离函数
def ur_disMeasure():
    GPIO.output(makerobo_TRIG,0) #开始计时
    time.sleep(0.000002)#延时两微秒
    GPIO.output(makerobo_TRIG,1) # 超声波启动信号，延时 10us
    time.sleep(0.00001)#发出超声波脉冲
    GPIO.output(makerobo_TRIG, 0)# 将引脚TRIG 设置为低电平
    while GPIO.input(makerobo_ECHO)== 0:#等待回传信号
        us_a = 0
    us_time1 = time.time()#获取当前时间
    while GPIO.input(makerobo_ECHO) == 1:#回传信号截止信息
        us_a = 1
    us_time2 = time.time()#获取当前时间
    us_during = us_time2 - us_time1#为徽秒级的时间
#声速在空气中的传播速度为 340m/s，超声波要经历一个发送信号和一个回传信号
#计算公式如下
    print(us_time1)
    print(us_time2)
    return us_during * 340/2 * 100  #求出距离
#循环函数
def makerobo_loop():
    while True:
        us_dis = ur_disMeasure()#获取超声波计算距离
        print(us_dis, 'cm') #打印超声波距离值
        print('-')
        time.sleep (0.3)#延时 300ms
#资源释放函数
def destroy() :
    GPIO.cleanup()#释放资源
#程序入口
if __name__=="__main__":
    makerobo_setup()#调用初始化函数
    try:
        makerobo_loop()#调用循环函数
    except KeyboardInterrupt:# 当按下Ctrl+C时，将执行 destroy()子程序
        destroy() #释放资源