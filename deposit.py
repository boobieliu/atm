#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'boobieliu'
from login import userinfo_save, consume_record_save
import time

def withdraw_deposit(userinfo_list, user_list):
    withdraw_number = raw_input("please input how much you want to deposit:").strip()
    if not withdraw_number.isdigit():
        print "pleas enter a number you less than %s" % (15000 + float(user_list[4]) * 1.05)
    else:
        print "you are going to deposit %s, and you quota is %s now." % (withdraw_number, \
                                                                         (15000 + float(user_list[4]) - float(withdraw_number)))
        n = userinfo_list.index(user_list)
        user_list[4] = str(float(user_list[4]) - float(withdraw_number) * 1.05)
        userinfo_list[n] = user_list
        userinfo_save("passwd.txt", userinfo_list)
        consume_time = str(time.strftime("%Y%m%d", time.localtime()))
        consume_record_list = [str(user_list[0]), '-' + str(withdraw_number), consume_time, 'atm', '取现']
        consume_record_save("transaction.txt", consume_record_list)

