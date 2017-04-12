#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'boobieliu'

from login import *
from query import *
from deposit import *
from repayment import *
from transfer import *
from consume import *

msg ='''
    please choose what you want to do:
    1:query
    2:deposit
    3:repayment
    4:transfer accounts
    5:consumption
    6:exit'''
if __name__ == '__main__':
    card_no, passwd = get_user_passwd()
    userinfo_list = get_userinfo_list("passwd.txt")
    consume_list = get_record_list('transaction.txt')
    if not userinfo_list:
        print "no user are in the system!"
        exit(3)
    user_list = verify_user(userinfo_list, card_no, passwd)
    i = 0
    while user_list and i < 5:
        print msg
        choice = raw_input("please input your choice(1-6):").strip()
        if choice.isdigit():
            if int(choice) == 1:
                query_user(userinfo_list, card_no)
                query_consume_record(consume_list, card_no)
            elif int(choice) == 2:
                withdraw_deposit(userinfo_list, user_list)
            elif int(choice) == 3:
                repayment(userinfo_list, user_list)
            elif int(choice) == 4:
                transfer_accounts(userinfo_list, user_list)
            elif int(choice) == 5:
                consume_record(userinfo_list, user_list)
            elif int(choice) == 6:
                exit("thank you for useing the atm system!")
            else:
                print 'wrong choice!! please enter the number between 1 and 6!'
        else:
            print "wrong iput, you must type a number!"
        i = i + 1