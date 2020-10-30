import sys


class Stack:
    _is_set = False

    def __init__(self, size):
        Stack._is_set = True
        self._count = 0
        self._list = [None for _ in range(size)]

    def push(self, new_item):
        if self._count < len(self._list):
            self._list[self._count] = new_item
            self._count += 1
        else:
            print("overflow")

    def pop(self):
        if self._count:
            self._count -= 1
            print(self._list[self._count])
        else:
            print("underflow")

    def print(self):
        if self._count:
            result = ""
            for item in self._list[:self._count]:
                result += str(item) + " "
            print(result[:-1])
        else:
            print("empty")

    @staticmethod
    def is_set():
        return Stack._is_set


input_commands = [cmd.replace("\n", "") for cmd in sys.stdin.readlines()]

for cmd in input_commands:
    if cmd[:8] == "set_size" and not Stack.is_set():
        stack = Stack(int(cmd[9:]))
    elif cmd[:4] == "push" and " " not in cmd[5:] and Stack.is_set():
        stack.push(cmd[5:])
    elif cmd == "pop" and Stack.is_set():
        stack.pop()
    elif cmd == "print" and Stack.is_set():
        stack.print()
    elif "" is not cmd:
        print("error")
