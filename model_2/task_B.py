import sys


class Node:
    """
    Класс Узел.
    Используется как узел "Косого дерева" (eng: "Splay tree").
    """
    def __init__(self, key: int, value: str) -> None:
        """
        Инициализация узла.

        :param key: Ключ узла (по нему производится сортировка).
        :param value: Значение узла (хранимые данные).
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_root(self) -> bool:
        """
        Является ли узел - корнем дерева.

        :return: True, если корень; False - если нет.
        """
        return self.parent is None

    def min(self):
        """
        Производит поиск наименьшего узлам по детям.

        :return: Наименьший узел (type: Node).
        """
        min_node = self
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def max(self):
        """
        Производит поиск наибольшего узлам по детям.

        :return: Наибольший узел (type: Node).
        """
        max_node = self
        while max_node.right is not None:
            max_node = max_node.right
        return max_node


class SplayTree:
    """
    Класс Косое дерево, или Расширяющееся дерево.
    Это двоичное дерево поиска, обладающее свойством сбалансированности.
    """
    def __init__(self) -> None:
        """
        Инициализация объекта.
        """
        self._root = None

    def _left_rotation(self, node: Node) -> None:
        """
        Малый левый поворот.
        Позволяет изменить структуру дерева, не меняя порядка элементов.
        Используется для уменьшения высоты дерева (его балансировки).

        :param node: Узел, осносительно которого производится левый поворот.
        """
        new_father = node.right
        node.right = new_father.left
        if new_father.left is not None:
            new_father.left.parent = node
        new_father.parent = node.parent

        if node.is_root():
            self._root = new_father
        elif node.parent.left == node:
            node.parent.left = new_father
        else:
            node.parent.right = new_father

        node.parent = new_father
        new_father.left = node

    def _right_rotation(self, node: Node) -> None:
        """
        Малый правый поворот.
        Позволяет изменить структуру дерева, не меняя порядка элементов.
        Используется для уменьшения высоты дерева (его балансировки).

        :param node: Узел, осносительно которого производится правый поворот.
        """
        new_father = node.left
        node.left = new_father.right
        if new_father.right is not None:
            new_father.right.parent = node
        new_father.parent = node.parent

        if node.is_root():
            self._root = new_father
        elif node.parent.left == node:
            node.parent.left = new_father
        else:
            node.parent.right = new_father

        node.parent = new_father
        new_father.right = node

    def _splay(self, new_root: Node) -> None:
        """
        Операция расширения - основная операция Косого дерева.
        Перемещает вершину "new_root" в корень дерева, используя Zig, Zig-Zig и Zig-Zag,
        которые, в свою очередь, оперируют малыми левым и правым разворотами в разных комбинациях.

        :param new_root: Вершина, которую требуется сделать новой вершиной.
        """
        while not new_root.is_root():
            if new_root.parent.is_root():
                if new_root.parent.left == new_root:
                    # Zag step.
                    self._right_rotation(new_root.parent)
                else:
                    # Zig step.
                    self._left_rotation(new_root.parent)
            elif new_root.parent.left == new_root:
                if new_root.parent.parent.left == new_root.parent:
                    # Zig-Zig step.
                    self._right_rotation(new_root.parent.parent)
                    self._right_rotation(new_root.parent)
                else:
                    # Zag-Zig step.
                    self._right_rotation(new_root.parent)
                    self._left_rotation(new_root.parent)
            else:
                if new_root.parent.parent.left == new_root.parent:
                    # Zig-Zag step.
                    self._left_rotation(new_root.parent)
                    self._right_rotation(new_root.parent)
                else:
                    # Zag-Zag step.
                    self._left_rotation(new_root.parent.parent)
                    self._left_rotation(new_root.parent)

    def search(self, key: int) -> None:
        """
        Ищет элемент по ключу в дереве. Также печатает его.

        :param key: Ключ искомого узла.
        """
        if self._root is not None:
            node = self._root
            while node.key != key:
                if key > node.key:
                    node = node.right
                else:
                    node = node.left

                if node is None:
                    print("0")
                    return

            print(f"1 {node.value}")
            self._splay(node)
        else:
            print("error")

    def min(self) -> Node:
        """
        Выдает наименьший элемент в дереве, предварительно печатая его.

        :return: Наименьший узел.
        """
        if self._root is not None:
            min_node = self._root.min()
            print(f"{min_node.key} {min_node.value}")
            return min_node
        else:
            print("error")

    def max(self) -> Node:
        """
        Выдает наибольший элемент в дереве, предварительно печатая его.

        :return: Наибольший узел.
        """
        if self._root is not None:
            max_node = self._root.max()
            print(f"{max_node.key} {max_node.value}")
            return max_node
        else:
            print("error")

    def _merge(self) -> None:
        """
        Соединяет два дерева.
        Используется при удалении элемента из дерева.
        """
        right_tree = self._root.right
        self._root = self._root.left
        right_tree.parent = None
        self._root.parent = None

        self._splay(self._root.max())
        right_tree.parent = self._root
        self._root.right = right_tree

    def delete(self, key: int) -> None:
        """
        Удаляет элемент из дерева по ключу.

        :param key: Ключ узла, который требуется удалить.
        """
        if self._root is not None:
            node = self._root
            while node.key != key:
                if key > node.key:
                    node = node.right
                else:
                    node = node.left

                if node is None:
                    print("error")
                    return

            self._splay(node)
            self._merge()
        else:
            print("error")

    def print(self, passed_nodes: list = None) -> None:
        """
        Печатает структуры Косого дерева.

        :param passed_nodes: Вершины, которые были пройдены в прошлой итерации.
        """
        if passed_nodes is None:
            passed_nodes = [self._root]
        new_passed_nodes = list()
        result = ""
        for node in passed_nodes:
            if node is None:
                new_passed_nodes.append(None)
                new_passed_nodes.append(None)
                result += "_ "
            else:
                new_passed_nodes.append(node.left)
                new_passed_nodes.append(node.right)
                if node.is_root():
                    result += f"[{node.key} {node.value}] "
                else:
                    result += f"[{node.key} {node.value} {node.parent.key}] "
        if "[" in result:
            print(result[:-1])
            self.print(new_passed_nodes)

    def add(self, key: int, value: str) -> None:
        """
        Добавляет узел с ключом "key" и значением "value".

        :param key: Ключ узла (по нему производится сортировка).
        :param value: Значение узла (хранимые данные).
        """
        new_node = Node(key, value)

        if self._root is None:
            self._root = new_node
        else:
            node = self._root
            while node.key != new_node.key:
                if new_node.key > node.key:
                    if node.right is not None:
                        node = node.right
                    else:
                        node.right = new_node
                        new_node.parent = node
                        break
                elif new_node.key < node.key:
                    if node.left is not None:
                        node = node.left
                    else:
                        node.left = new_node
                        new_node.parent = node
                        break
                else:
                    print("error")
                    return

            self._splay(new_node)

    def set(self, key: int, value: str) -> None:
        """
        Заменяет значение в узле с ключом "key" на "value".

        :param key: Ключ узла (по нему производится сортировка).
        :param value: Значение узла (хранимые данные).
        """
        if self._root is not None:
            node = self._root
            while node.key != key:
                if key > node.key:
                    node = node.right
                else:
                    node = node.left

                if node is None:
                    print("error")
                    return

            node.value = value
            self._splay(node)
        else:
            print("error")


if __name__ == "__main__":
    input_commands = [cmd.replace("\n", "") for cmd in sys.stdin.readlines()]
    tree = SplayTree()

    for cmd in input_commands:
        if cmd[:3] == "add":
            params = cmd[4:].split()
            tree.add(int(params[0]), params[1])
        elif cmd[:3] == "set":
            params = cmd[4:].split()
            tree.set(int(params[0]), params[1])
        elif cmd[:6] == "delete":
            tree.delete(int(cmd[7:]))
        elif cmd[:6] == "search":
            tree.search(int(cmd[7:]))
        elif cmd == "min":
            tree.min()
        elif cmd == "max":
            tree.max()
        elif cmd == "print":
            tree.print()
        elif "" is not cmd:
            print("error")
