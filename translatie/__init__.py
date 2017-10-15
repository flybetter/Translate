#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Translate
@file= __init__.py
@author= wubingyu
@create_time= 2017/10/7 下午8:04
"""
import os
import re
import time
from threading import Timer



# schedule = sched.scheduler(time.time(), time.sleep())


def getfilename(filePath):
    files = os.listdir(filePath)
    for fileName in files:
        if re.match(r"^(.*)python(.*)$", fileName):
            return fileName


def sche(filePath):
    result = getfilename(filePath)
    if not result:
        print result
        Timer(0, sche, (filePath,)).start()
    else:
        print "fileName:" + result


def translate(oldPath, newPath):
    status = os.system("date")
    print status




if __name__ == "__main__":
    path = "/Users/wubingyu/Downloads"
    # filename = getfilename(path)
    # print filename
    # sche(path)
    # main("netstat -an", 60)
    # Timer(5, func, ('hello', time.time())).start()
    # Timer(3, sche, (path,)).start()
    translate("11", "22")
