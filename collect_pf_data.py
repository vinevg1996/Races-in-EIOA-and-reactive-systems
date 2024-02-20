#! /usr/bin/python
import sys, string, os

dig_dict_1 = dict()
dig_dict_2 = dict()

N = 1000
for i in range(0, N):
    print("i = ", i)
    os.system("cat /dev/null > rules_out.txt")
    pf_argv_str = '(time ./pf_argv_time {}) > rules_out.txt 2>&1'.format(1)
    os.system(pf_argv_str)
    f_in = open("rules_out.txt", 'r')
    for line in f_in:
        if ("user" in line):
            str_list = line.split(" ")
            len2 = len(str_list[2])
            time = str(str_list[2][3:len2 - 7])
            dig = float(time)
            if (dig in dig_dict_1.keys()):
                dig_dict_1[dig] = dig_dict_1[dig] + 1
            else:
                dig_dict_1[dig] = 1
            print("dig_time = ", dig)
    os.system("./df_all")

for i in range(0, N):
    print("i = ", i)
    os.system("cat /dev/null > rules_out.txt")
    pf_argv_str = '(time ./pf_argv_time {}) > rules_out.txt 2>&1'.format(2)
    os.system(pf_argv_str)
    f_in = open("rules_out.txt", 'r')
    for line in f_in:
        if ("user" in line):
            str_list = line.split(" ")
            len2 = len(str_list[2])
            time = str(str_list[2][3:len2 - 7])
            dig = float(time)
            if (dig in dig_dict_2.keys()):
                dig_dict_2[dig] = dig_dict_2[dig] + 1
            else:
                dig_dict_2[dig] = 1
            print("dig_time = ", dig)
    os.system("./df_all")

print("dig_dict_1:")
for dig in dig_dict_1.keys():
    print(dig, ":", dig_dict_1[dig])
print("dig_dict_2:")
for dig in dig_dict_2.keys():
    print(dig, ":", dig_dict_2[dig])
