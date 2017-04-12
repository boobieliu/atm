#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'boobieliu'

#查询用户信息
def query_user(userinfo_list, card_no):
    for n in range(len(userinfo_list)):
        if card_no == userinfo_list[n][0]:
            print 'Hello, dear %s'% userinfo_list[n][3]
            if  userinfo_list[n][4] <= 15000:
                print "you quota is run out!"
            else:
                print 'your accout have %s quota' % (15000 + float(userinfo_list[n][4]))

#查询用户交易记录
def query_consume_record(consume_list, card_no):
    if not consume_list:
        print "there is no record here!"
        return None
    for n in range(len(consume_list)):
        if card_no == consume_list[n][0]:
            print "you consum record as follows"
            print "consume_money: {0}, consume_date: {1}, consume_location: {2}, consume_comment: {3}"\
            .format(consume_list[n][1], consume_list[n][2], consume_list[n][3], consume_list[n][4])
    else:
        print "you have no record this month!"
