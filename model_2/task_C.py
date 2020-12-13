from math import log2
import sys
from typing import List


class BinaryNode:
    """
    Класс Узел.
    Используется как узел "Двоичной кучи" (eng: "Binary heap" or "Min Heap").
    """
    def __init__(self, key: int, value: str) -> None:
        """
        Инициализация узла.

        :param key: Ключ узла.
        :param value: Значение узла.
        """
        self.key = key
        self.value = value


class BinaryHeap:
    """
    Класс Двоичная куча, или Двоичная min-куча.

    Это двоичное дерево с двумя дополнительными ограничениями:
    1) Shape property: "Все уровни дерева, кроме последнего, должны быть заполнены.
    Последний уровень должен быть заполнен слева направо".
    2) Heap property: "Ключ в узел строго меньше ключей дочерних узлов".
    """
    def __init__(self) -> None:
        """
        Инициализация кучи.
        """
        # Список узлов (нод) кучи.
        self._list_of_nodes = []

        # Словарь, в котором ключи - это ключи узлов,
        # а значения - индексы узлов в self._list_of_nodes.
        self._key_to_index_map = dict()

    def _heapify(self, new_root_key: int) -> None:
        """
        Восстанавливает основные свойства кучи для дерева с новым корнем.

        Условие: оба поддерева должны удовлетворять условия Двоичной кучи.
        :param new_root_key: Ключ узла, который требуется сделать новым root-узлом.
        """
        new_root_index = self._key_to_index_map[new_root_key]

        index_of_left_child = 2 * new_root_index + 1
        index_of_right_child = 2 * new_root_index + 2

        if index_of_right_child < len(self._list_of_nodes):
            key_of_left_child = self._list_of_nodes[index_of_left_child].key
            key_of_right_child = self._list_of_nodes[index_of_right_child].key
        elif index_of_left_child < len(self._list_of_nodes):
            key_of_left_child = self._list_of_nodes[index_of_left_child].key
            key_of_right_child = None
        else:
            key_of_left_child = None
            key_of_right_child = None

        if index_of_left_child < len(self._list_of_nodes):
            if key_of_left_child is not None or key_of_right_child is not None:
                if key_of_left_child is None:
                    key_of_smaller_child = key_of_right_child
                    index_of_smaller_child = index_of_right_child
                elif key_of_right_child is None:
                    key_of_smaller_child = key_of_left_child
                    index_of_smaller_child = index_of_left_child
                elif key_of_left_child < key_of_right_child:
                    key_of_smaller_child = key_of_left_child
                    index_of_smaller_child = index_of_left_child
                else:
                    key_of_smaller_child = key_of_right_child
                    index_of_smaller_child = index_of_right_child
                if new_root_key > key_of_smaller_child:
                    self._list_of_nodes[new_root_index], self._list_of_nodes[index_of_smaller_child] = \
                        self._list_of_nodes[index_of_smaller_child], self._list_of_nodes[new_root_index]
                    self._key_to_index_map[new_root_key], self._key_to_index_map[key_of_smaller_child] = \
                        self._key_to_index_map[key_of_smaller_child], self._key_to_index_map[new_root_key]

                    self._heapify(new_root_key)
                    return

        index_of_parent = (new_root_index - 1) // 2

        if index_of_parent >= 0:
            key_of_parent = self._list_of_nodes[index_of_parent].key

            if key_of_parent > new_root_key:
                self._list_of_nodes[new_root_index], self._list_of_nodes[index_of_parent] = \
                    self._list_of_nodes[index_of_parent], self._list_of_nodes[new_root_index]
                self._key_to_index_map[new_root_key], self._key_to_index_map[key_of_parent] = \
                    self._key_to_index_map[key_of_parent], self._key_to_index_map[new_root_key]

                self._heapify(new_root_key)

    def add(self, new_key: int, new_value: str) -> None:
        """
        Добавляет новый узел в кучу.

        :param new_key: Ключ нового узла, который требуется добавить.
        :param new_value: Значение нового узла, который требуется добавить.
        """
        if new_key not in self._key_to_index_map:
            new_node = BinaryNode(new_key, new_value)
            self._key_to_index_map[new_key] = len(self._list_of_nodes)
            self._list_of_nodes.append(new_node)
            self._heapify(new_key)
        else:
            print("error")

    def set(self, key: int, new_value: str) -> None:
        """
        Изменяет данные узла (значение в узле) по ключу.

        :param key: Ключ узла, которые требуется изменить.
        :param new_value: Новое значение для узла.
        """
        if key in self._key_to_index_map:
            index_of_old_node = self._key_to_index_map[key]
            self._list_of_nodes[index_of_old_node].value = new_value
        else:
            print("error")

    def delete(self, key: int) -> None:
        """
        Удаление узла из кучи по ключу.

        :param key: Ключ узла, который нужно удалить.
        """
        if key in self._key_to_index_map:
            node_index = self._key_to_index_map[key]
            self._key_to_index_map.pop(key)

            if node_index == len(self._list_of_nodes) - 1:
                self._list_of_nodes = self._list_of_nodes[:-1]
            else:
                self._list_of_nodes = self._list_of_nodes[:node_index] +\
                                      [self._list_of_nodes[-1]] +\
                                      self._list_of_nodes[node_index + 1:-1]
                self._key_to_index_map[self._list_of_nodes[node_index].key] = node_index

                self._heapify(self._list_of_nodes[node_index].key)
        else:
            print("error")

    def search(self, searched_key: int) -> BinaryNode:
        """
        Ищет узел по ключу и печатает его.

        Если узел с таким ключом существует в куче, то
        печать производится в формате "1 INDEX VALUE",
        где INDEX - индекс искомого узла в self._list_of_nodes,
            VALUE - значение искомого узла;
        если узел с таким ключом не был найдет, то печатается "0".

        :param searched_key: Ключ искомого узла.
        :return: Искомый узел.
        """
        if searched_key in self._key_to_index_map:
            index_of_searched_node = self._key_to_index_map[searched_key]

            print(f"1 {index_of_searched_node} {self._list_of_nodes[index_of_searched_node].value}")
            return self._list_of_nodes[index_of_searched_node]
        else:
            print("0")

    def min(self) -> BinaryNode:
        """
        Ищет узел с минимальным ключом и печатает его.

        Печать производится в формате "MIN_KEY INDEX VALUE",
        где MIN_KEY - ключ минимального узла,
            INDEX   - индекс минимального узла в self._list_of_nodes (всегда '0'),
            VALUE   - значение минимального узла.

        :return: Минимальный узел в куче.
        """
        if len(self._list_of_nodes):
            print(f"{self._list_of_nodes[0].key} 0 {self._list_of_nodes[0].value}")
            return self._list_of_nodes[0]
        else:
            print("error")

    def max(self) -> BinaryNode:
        """
        Ищет узел с максимальным ключом и печатает его.

        Печать производится в формате "MAX_KEY INDEX VALUE",
        где MAX_KEY - ключ максимального узла,
            INDEX   - индекс максимального узла в self._list_of_nodes,
            VALUE   - значение максимального узла.

        :return: Максимальный узел в куче.
        """
        if len(self._list_of_nodes):
            potentially_max_nodes = self._list_of_nodes[-(len(self._list_of_nodes) - (len(self._list_of_nodes) // 2)):]

            max_node = potentially_max_nodes[0]
            for node in potentially_max_nodes:
                if max_node.key < node.key:
                    max_node = node

            print(f"{max_node.key} {self._key_to_index_map[max_node.key]} {max_node.value}")
            return max_node
        else:
            print("error")

    def extract(self) -> None:
        """
        Печатает, а затем удаляет корневой узел из кучи.

        Печать производится в формате "ROOT_KEY ROOT_VALUE",
        где ROOT_KEY   - ключ корневого узла,
            ROOT_VALUE - значение корневого узла.
        """
        print(f"{self._list_of_nodes[0].key} {self._list_of_nodes[0].value}")
        self.delete(self._list_of_nodes[0].key)

    def print(self) -> None:
        """
        Печатает кучу.

        Печать корневого узла прозводится в формате "[ROOT_KEY ROOT_VALUE]",
        где ROOT_KEY   - ключ корневого узла,
            ROOT_VALUE - значение корневого узла;
        печать остальных узлов производится в формате "[KEY VALUE PARENT_KEY]",
        где KEY        - ключ узла,
            VALUE      - значение узла,
            PARENT_KEY - ключ родительского узла.
        Если требуемый узел не существует, печатается "_".
        Узлы одного уровня разделяются пробелом (space, " ").
        """

        def get_print_blocks_without_root(list_of_nodes: List[BinaryNode]) -> List:
            """
            Генериует блоки узлов для печати.
            Узлы распалагаются по уровням печати.

            :param list_of_nodes: Список узлов.
            :return: Блоки узлов, подготовленные для печати.
            """
            result = []

            for i in range(1, int(log2(len(list_of_nodes)) + 1)):
                nodes_on_level = list_of_nodes[2**i - 1:2*2**i - 1]
                nodes_on_level += ['_ '] * (2*2**i - 2**i - len(nodes_on_level))
                result.append(nodes_on_level)

            return result

        if len(self._list_of_nodes):
            print(f"[{self._list_of_nodes[0].key} {self._list_of_nodes[0].value}]")

            level_blocks_for_print = get_print_blocks_without_root(self._list_of_nodes)

            for level_block in level_blocks_for_print:
                string_for_print = ''

                for node in level_block:
                    if isinstance(node, BinaryNode):
                        parent_index = (self._key_to_index_map[node.key] - 1) // 2
                        parent_key = self._list_of_nodes[parent_index].key

                        string_for_print += f"[{node.key} {node.value} {parent_key}] "
                    else:
                        string_for_print += node

                print(string_for_print[:-1])
        else:
            print('_')


if __name__ == '__main__':
    input_commands = [cmd.replace('\n', '') for cmd in sys.stdin.readlines()]
    heap = BinaryHeap()

    for cmd in input_commands:
        if cmd[:3] == "add":
            params = cmd[4:].split()
            heap.add(int(params[0]), params[1])
        elif cmd[:3] == "set":
            params = cmd[4:].split()
            heap.set(int(params[0]), params[1])
        elif cmd[:6] == "delete":
            heap.delete(int(cmd[7:]))
        elif cmd[:6] == "search":
            heap.search(int(cmd[7:]))
        elif cmd == "min":
            heap.min()
        elif cmd == "max":
            heap.max()
        elif cmd == "extract":
            heap.extract()
        elif cmd == "print":
            heap.print()
        elif cmd != "":
            print("error")
