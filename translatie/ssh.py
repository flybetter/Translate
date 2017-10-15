#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Translate
@file= ssh
@author= wubingyu
@create_time= 2017/10/8 下午7:38
"""
from pexpect import pxssh
import re


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    # print s.before
    return s.before


def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print "error"
        exit(0)


def main():
    s = connect("10.245.250.38", "root", "cmsroot")
    result = send_command(s, "ps -ef|grep java")
    line = result.split('\r')[4]
    print line
    print re.findall(r"\S\w*/\w*/java", line)



if __name__ == '__main__':
    main()
