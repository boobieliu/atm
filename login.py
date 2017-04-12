#!/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'boobieliu'

#获取用户输入
def get_user_passwd():
    print '-----------------------------------------------------------'
    print '------------welcome to the atm system----------------------'
    for i in range(5):
        card_no = raw_input("please input you card no:").strip()
        passwd = raw_input("please input you passwd:").strip()
        if  not card_no.isdigit() or len(card_no) != 12:
            print "please type 12 numeral card number or 5 numeral passwd! you still have %s chances"% (5 - i - 1)
            continue
        if not passwd.isdigit() or len(passwd) != 6:
            print "please type 12 numeral card number or 5 numeral passwd! you still have %s chances" % (5 - i - 1)
            continue
        return card_no,passwd
    exit('you had enter 5 times wrong number or passwd')

#读取密码配置文件
def get_userinfo_list(passwd_file):
    passwd_file = open(passwd_file, 'r')
    line_of_all_passwd = passwd_file.readlines()
    if line_of_all_passwd:
        userinfo_list = []
        for line in line_of_all_passwd:
            line = line.strip('\n')
            lines = line.split(':')
            userinfo_list.append(lines)
        return userinfo_list

#获取消费记录文件
def get_record_list(consume_file_name):
    consume_file = open(consume_file_name, 'r')
    line_of_all_consume = consume_file.readlines()
    if line_of_all_consume:
        consume_list = []
        for line in line_of_all_consume:
            line = line.strip('\n')
            lines = line.split(':')
            consume_list.append(lines)
        return consume_list

#保存至文件
def userinfo_save(passwd_file, userinfo_list):
    fl = open(passwd_file, 'w')
    for i in userinfo_list:
        str_list = ':'.join(i)
        fl.write(str_list)
        fl.write("\n")
    fl.close()

#密码匹配
def verify_user(userinfo_list, your_name, your_passwd):

    for n in range(len(userinfo_list)):
        if your_name == userinfo_list[n][0]:
            if int(userinfo_list[n][2]) < 3:
                if your_passwd == userinfo_list[n][1]:
                    print "welcome %s" % (userinfo_list[n][3])
                    userinfo_list[n][2] = str(0)
                    userinfo_save("passwd.txt", userinfo_list)
                    return userinfo_list[n]
                else:
                    print "1you enter the wrong username or passwd!"
                    userinfo_list[n][2] = str(int(userinfo_list[n][2]) + 1)
                    userinfo_save("passwd.txt", userinfo_list)
                    break
            else:
                print "2your accout had been locked!"
                userinfo_save("passwd.txt", userinfo_list)
                exit(1)
    else:
        print "3you enter the wrong username or passwd"

#消费记录文件保存
def consume_record_save(consume_file_name, consume_record):
    fl = open(consume_file_name, 'a')
    str_list = ':'.join(consume_record)
    fl.write(str_list)
    fl.write("\n")
    fl.close()

if __name__ == '__main__':
    get_user_passwd()