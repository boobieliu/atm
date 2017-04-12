#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'boobieliu'

from login import userinfo_save
from login import consume_record_save
import time

def repayment(userinfo_list, user_list):
    repayment_member = raw_input("please input how much you want to deposit:").strip()
    if not repayment_member.isdigit() or float(repayment_member) > (15000 + float(user_list[4])):
        print "wrong input! pleas enter a number you want to repayment your card!"
    else:
        print "you are going to deposit %s, and you quota is %s now." % (repayment_member, \
                                                                         (15000 + float(user_list[4]) + float(repayment_member)))
        n = userinfo_list.index(user_list)
        user_list[4] = str(float(user_list[4]) + float(repayment_member))
        userinfo_list[n] = user_list
        userinfo_save("passwd.txt", userinfo_list)
        consume_time = str(time.strftime("%Y%m%d", time.localtime()))
        consume_record_list = [str(user_list[0]), '+' + str(repayment_member), consume_time, 'atm', '还款']
        consume_record_save("transaction.txt", consume_record_list)
