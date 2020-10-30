import sys


class Queue:
    _is_set = False
    _output = open(sys.argv[2], 'w')

    def __init__(self, size):
        Queue._is_set = True
        self._index_of_first = 0
        self._length = 0
        self._list = [None for _ in range(size)]

    def push(self, new_item):
        if self._length < len(self._list):
            self._list[(self._index_of_first + self._length) % len(self._list)] = new_item
            self._length += 1
        else:
            Queue._output.write("overflow\n")

    def pop(self):
        if self._length:
            del_item = self._list[self._index_of_first]
            self._index_of_first = (self._index_of_first + 1) % len(self._list)
            self._length -= 1
            Queue._output.write(del_item + "\n")
        else:
            Queue._output.write("underflow\n")

    def print(self):
        if self._length:
            result = ""
            for index in range(self._length):
                result += self._list[(self._index_of_first + index) % len(self._list)] + " "

            Queue._output.write(result[:-1] + "\n")
        else:
            Queue._output.write("empty\n")

    @staticmethod
    def is_set():
        return Queue._is_set

    @staticmethod
    def write_error():
        Queue._output.write("error\n")


input_commands = [line.replace("\n", "") for line in open(sys.argv[1], 'r')]

for cmd in input_commands:
    if cmd[:8] == "set_size" and not Queue.is_set():
        stack = Queue(int(cmd[9:]))
    elif cmd[:4] == "push" and " " not in cmd[5:] and Queue.is_set():
        stack.push(cmd[5:])
    elif cmd == "pop" and Queue.is_set():
        stack.pop()
    elif cmd == "print" and Queue.is_set():
        stack.print()
    elif "" is not cmd:
        Queue.write_error()
