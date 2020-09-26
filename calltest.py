# coding:utf-8
from time import sleep
import time, os, random


def autocalltest(callnumber):
    call=os.popen('adb shell am start -a android.intent.action.CALL -d tel:%s' % callnumber)
    sleep(20)
    screenshot=os.popen("adb shell /system/bin/screencap -p /sdcard/pic{}.png".format(i))
    sleep(5)
    SaveScreenShot = os.popen("adb pull /sdcard/pic{}.png ./pic".format(i) )
    sleep(5)
    endcall=os.popen('adb shell input keyevent 6')
    sleep(10)
if __name__ == '__main__':
    call_number_list = [122, 114, 10086, 12580, 12345]
    for i in range(100):
        callnumber = random.choice(call_number_list)
        print("第%s次拨打电话测试"%i)
        print('电话号码是:%s' % callnumber)
        autocalltest(callnumber)