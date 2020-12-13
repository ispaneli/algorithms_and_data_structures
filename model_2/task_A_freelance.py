from sys import stdin
from math import log, log2


WAS_CREATED = False


class __BloomException(Exception):
    pass


def __get_prime_numbers(count):
    result = list()

    for i in range(count):
        if not len(result):
            result.append(2)
            continue
        next_number = 1 + result[len(result) - 1]
        while True:
            flag = False
            for j in result:
                if not next_number % j:
                    flag = True
                    break
            if flag:
                next_number += 1
            else:
                result.append(next_number)
                break

    return result


def check_error(function):
    def new_function(*args):
        try:
            if args[1] <= 0:
                raise __BloomException
            elif args[2] <= 0 or args[2] >= 1:
                raise __BloomException
            else:
                size = -round(log2(args[2]) / log(2) * args[1])
                count = -round(log2(args[2]))
                if size <= 0:
                    raise __BloomException
                elif count <= 0:
                    raise __BloomException
                else:
                    prime_numbers = __get_prime_numbers(count)
                    function(args[0], size, count, prime_numbers)
                    global WAS_CREATED
                    WAS_CREATED = True
        except __BloomException:
            print('error')
    return new_function


class FilterOfBloom:
    @check_error
    def __init__(self, size, count, prime_numbers):
        print(size, count)
        self.__size = size
        self.__count = count
        self.__filter = 0
        self.__mersene = 2**31 - 1
        self.__prime_numbers = prime_numbers

    def add_item(self, item):
        for i in range(self.__count):
            hash_move = 1 << (((self.__prime_numbers[i] + i*item + item)%self.__mersene)%self.__size)
            self.__filter |= hash_move

    def print_filter(self):
        filter = F'{self.__filter:b}'
        filter = '0' * (self.__size - len(filter)) + filter
        print(filter[::-1])

    def search_item(self, item):
        for i in range(self.__count):
            hash_move = 1 << (((self.__prime_numbers[i] + i*item + item)%self.__mersene)%self.__size)
            if not self.__filter&hash_move:
                print('0')
                return
        print('1')


for line in stdin:
    if WAS_CREATED:
        if 'add' == line[:3]:
            item = int(line[4:])
            filter_of_bloom.add_item(item)
        elif 'search' == line[:6]:
            item = int(line[7:])
            filter_of_bloom.search_item(item)
        elif 'print' == line[:5]:
            filter_of_bloom.print_filter()
        elif len(line) > 1:
            print('error')
    else:
        if 'set' == line[:3]:
            numbers = line[4:].split(' ')
            size = int(numbers[0])
            count = float(numbers[1])
            filter_of_bloom = FilterOfBloom(size, count)
        elif len(line) > 1:
            print('error')
