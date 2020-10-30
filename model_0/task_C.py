import sys

# print('agrv:', sys.argv)
in_filename = sys.argv[1]
out_filename = sys.argv[2]
# raise Exception(sys.argv)

# in_filename = input()
# out_filename = input()

res = 0

in_f = open(in_filename, 'r')
# for line in in_f:
#     try:
#         num = int(line)
#         res += num
#     except Exception:
#         pass
message = [line for line in in_f]


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

out_f = open(out_filename, 'w')
out_f.write(str(res % 256))