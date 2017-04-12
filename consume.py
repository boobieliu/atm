#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'boobieliu'

from login import userinfo_save, consume_record_save
import  time

def consume_record(userinfo_list, user_list):
    for i in range(5):
        consume_number = raw_input("how much have you consume?").strip()
        if not consume_number.isdigit() or float(consume_number) > 15000 + float(user_list[4]):
            print "you must input a number less than %s!" %(15000 + int(user_list[4]))
            continue
        elif  float(user_list[4]) - float(consume_number) <= -15000:
            print "you must input a number less than %s!" % (15000 + float(user_list[4]))
            continue
        consume_time = str(time.strftime("%Y%m%d", time.localtime()))
        consume_location = raw_input("type where your consume?").strip()
        consume_comment = raw_input("type what your consume?").strip()
        consume_record_list =[str(user_list[0]),'-' + str(consume_number), consume_time, consume_location, consume_comment]
        consume_record_save("transaction.txt", consume_record_list)
        print consume_record_list
        for n in range(len(userinfo_list)):
            n = userinfo_list.index(user_list)
            user_list[4] = str(float(user_list[4]) - float(consume_number))
            userinfo_list[n] = user_list
            userinfo_save("passwd.txt", userinfo_list)
            return None
