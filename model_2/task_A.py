import math
import sys
from typing import List


class BloomFilter:
    # 31-ое число Мерсенна (ряд, элементы которого вычисляются как: 2^n - 1)
    _thirty_first_of_Mersenne = 2 ** 31 - 1
    _is_set = False

    def __init__(self, elem_count: int, prob_of_fp: float) -> None:
        """
        Инициализация объекта.

        :param elem_count: Приблизительное количество элементов (обязательное целое). Иначе: параметр "n".
        :param prob_of_fp: Вероятность ложноположительного ответа (0 < prob_of_fp < 1). Иначе: параметр "P".
        """
        if elem_count <= 0 or prob_of_fp <= 0 or prob_of_fp >= 1:
            print("error")
            return

        # Размер структуры (иначе: параметр "m"): m = -n * log2(P) / ln(2)
        # Затем округление в сторону ближайшего целого.
        self._size = round(-elem_count * math.log(prob_of_fp, 2) / math.log(2))
        self._bits = 0

        # Количество хеш-функций (иначе: параметр "k"): k = -log2(P)
        # Затем округление в сторону ближайшего целого.
        self._hf_count = round(-math.log(prob_of_fp, 2))

        if self._size <= 0 or self._hf_count <= 0:
            print("error")
            return

        self._prime_nums = self._generate_prime_numbers()
        BloomFilter._is_set = True

        print(self._size, self._hf_count)

    def _hash_function(self, index: int, key: int) -> int:
        """
        Вычисляет значение i-той хеш-функции.
        Формула хеш-функций: hi(x) = (((i + 1) * x + p[i + 1]) mod M) mod m, где
        x - ключ, i - номер хэш-функции, pi - i-тое по счету простое число, а M - 31-ое число Мерсенна.

        :param index: Номер хеш-функции. Иначе: параметр "i".
        :param key: Значение, чей хеш выдает Иначе: параметр "x".
        :return: Хеш ключа (параметра "x") в диапазоне от 0 до self._size не включительно.
        """
        return (((index + 1) * key + self._prime_nums[index]) % self._thirty_first_of_Mersenne) % self._size

    def _generate_prime_numbers(self) -> List[int]:
        """
        Функция генерации простых чисел для работы хеш-функций.

        :return: Список простых чисел.
        """
        def is_prime_number(prev_prime_nums, new_num):
            for prime_num in prev_prime_nums:
                if not new_num % prime_num:
                    return False
            return True

        prime_nums = []

        for _ in range(self._hf_count):
            if prime_nums:
                new_prime_num = prime_nums[-1] + 1
                while not is_prime_number(prime_nums, new_prime_num):
                    new_prime_num += 1
                prime_nums.append(new_prime_num)
            else:
                prime_nums.append(2)

        return prime_nums

    def add(self, new_elem: int) -> None:
        """
        Добавление в фильтр Блума нового элемента.

        :param new_elem: Добавляемый элемент.
        """
        new_bits = self._bits
        for index in range(self._hf_count):
            new_bits |= 1 << self._hash_function(index, new_elem)
        else:
            self._bits = new_bits

    def search(self, elem: int) -> bool:
        """
        Поиска элемента в фильтре Блума. Ответ печатается в стандартный поток вывода.

        :param elem: Элемент, который ищем.
        :return: True, если элемент "возможно есть" в фильтре; False - если элемента "нет".
        """
        for index in range(self._hf_count):
            if not self._bits & 1 << self._hash_function(index, elem):
                print("0")
                return False
        print("1")
        return True

    def print(self) -> str:
        """
        Печатает в стандартный поток вывода набор битов в фильтре Блума.

        :return: Строку с набором битов.
        """
        result = f"{self._bits:b}"

        while len(result) != self._size:
            result = "0" + result
        result = result[::-1]

        print(result)
        return result

    @staticmethod
    def is_set() -> bool:
        """
        Был ли фильтр Блума уже инициализирован.

        :return: True, если был инициализирован; False - если нет.
        """
        return BloomFilter._is_set


if __name__ == "__main__":
    input_commands = [cmd.replace("\n", "") for cmd in sys.stdin.readlines()]

    for cmd in input_commands:
        if cmd[:3] == "set" and not BloomFilter.is_set():
            params = cmd[4:].split()
            filter = BloomFilter(int(params[0]), float(params[1]))
        elif cmd[:3] == "add" and BloomFilter.is_set():
            filter.add(int(cmd[4:]))
        elif cmd[:6] == "search" and BloomFilter.is_set():
            filter.search(int(cmd[7:]))
        elif cmd == "print" and BloomFilter.is_set():
            filter.print()
        elif "" is not cmd:
            print("error")
