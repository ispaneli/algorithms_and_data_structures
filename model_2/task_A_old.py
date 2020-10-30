import math

class BloomFilter:
    def __init__(self, n: int, P: float):
        # n - приблизительное количество элементов (целое), P - вероятность ложноположительного ответа.
        # 0 <= P <= 1

        # m = -n * log2 P / ln 2
        # И округление в строну ближайшего целого.
        # m - это размер структуры.
        self._m = round(-n * math.log(P, 2) / math.log(2))
        # self.bites = [bytearray(math.ceil(self._m / 8))]
        self.bites = [None for _ in range(self._m)]

        # k - количество хэш-функций.
        self._k = round(-math.log(P, 2))
        print(self._m, self._k)

    def _get_hash_function(self, index, key):
        return (((index + 1) * key  + BloomFilter._get_prostoe_chislo(index + 1)) % BloomFilter._get_prostoe_chislo(31)) % self._m

    @staticmethod
    def _get_prostoe_chislo(index):
        # Method: Sieve of Eratosthenes
        count = 1
        i = 1
        D = {}
        n = index
        m = int(n * (math.log(n) + math.log(math.log(n))))
        while count < n:
            i += 2
            if i not in D:
                count += 1
                k = i * i
                if k > m:
                    break
                while k <= m:
                    D[k] = 0
                    k += 2 * i
        while count < n:
            i += 2
            if i not in D:
                count += 1
        if i >= m:
            print("invalid: top value estimate too small", i, m)
        print(i, m)
        return i

    def print(self):
        result = ""
        for i in range(self._m):
            result +=



BloomFilter(2, 0.250)
print(BloomFilter._get_prostoe_chislo(168))

