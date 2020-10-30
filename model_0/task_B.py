# res = 0
#
# for _ in range(100):
#     try:
#         num = int(input())
#     except Exception:
#         pass
#     print(num)
#     res += num
#
# print(res)

import sys


message = sys.stdin.readlines()
#message = [">_<","1:)2>:=->",":-3","8)","]:->","o_0","(*V*)"]
res = 0
jojo = "0123456789"
new_mess = []
if len(message) > 1:
    for num in message:
        new_num = num
        for i in range(len(num)):
            if num[i] == '-':
                #print(f"len(num) > i + 1: {len(num) > i + 1}, num = {num}, i = {i}")
                #print(f"num[i + 1] not in jojo: {num[i + 1] not in jojo}")
                if len(num) > i + 1 and num[i + 1] not in jojo:
                    new_num = new_num[:i] + ' ' + new_num[i + 1:]
                    #new_num[i + 1] = ' '
            elif num[i] not in jojo:
                if len(new_num) > i + 1:
                    new_num = new_num[:i] + ' ' + new_num[i + 1:]
                else:
                    new_num = new_num[:i] + ' '
        new_mess.append(new_num)
    message = new_mess
    #print(message)

for num in message:
    try:
        nums = [int(i) for i in num.split()]
        res += sum(nums)
    except Exception:
        try:
            nums = [int(i) for i in num.split(',')]
            res += sum(nums)
        except Exception:
            try:
                nums = [int(i) for i in num.split('_')]
                res += sum(nums)
            except Exception:
                try:
                    int_num = int(num)
                    res += int_num
                except Exception:
                    pass

print(res)
