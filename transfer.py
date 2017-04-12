#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'boobieliu'
from login import userinfo_save

def transfer_accounts(userinfo_list, user_list):
    for i in range(5):
        transfer_account = raw_input("please enter who you want to transfer:").strip()
        if  not transfer_account.isdigit() or len(transfer_account) != 12:
            print "wrong accout! please type a 12 digits"
        elif int(transfer_account) == int(user_list[0]):
            print "you cann't transfer to yourself!"
        else:
            for n in range(len(userinfo_list)):
                if int(transfer_account) == int(userinfo_list[n][0]) \
                        and int(transfer_account) != int(user_list[0]):
                    print userinfo_list[n][0]
                    for i in range(5):
                        transfer_member = raw_input("please enter the number you want to transfer to:").strip()
                        if not transfer_member.isdigit() or float(transfer_member) > (15000 \
                                                                                    + float(user_list[4])):
                            print "wront nukber! please enter a number less than %s!" %((15000 \
                                                                                    + float(user_list[4])))
                        else :
                            roll_out_index = userinfo_list.index(user_list)
                            userinfo_list[n][4] = str(float(transfer_member) +  float(userinfo_list[n][4]))
                            user_list[4] = str(float(user_list[4]) - float(transfer_member))
                            userinfo_list[roll_out_index] = user_list
                            userinfo_save("passwd.txt", userinfo_list)
                            return None
                    else:
                        print "you have enter 5 times wrong transfer number!"
            else:
                print "you have enter 5 times wront transfer account!"