from sys import stdin


class SplayTree:
    def __init__(self):
        self.__root_node = None

    def add(self, key, value):
        class Node:
            def __init__(self, key, value):
                self.parent_node = None
                self.left_node = None
                self.right_node = None

                self.key = key
                self.value = value

            def search_min_node(self):
                if self.left_node is None:
                    return self
                else:
                    node = self.left_node
                    while node.left_node is not None:
                        node = node.left_node
                    return node

            def search_max_node(self):
                if self.right_node is None:
                    return self
                else:
                    node = self.right_node
                    while node.right_node is not None:
                        node = node.right_node
                    return node

        new_node = Node(key, value)
        if self.__root_node is None:
            self.__root_node = new_node
            return
        main_node = self.__root_node
        while True:
            if new_node.key < main_node.key:
                if main_node.left_node is not None:
                    main_node = main_node.left_node
                else:
                    main_node.left_node = new_node
                    new_node.parent_node = main_node
                    break
            elif new_node.key > main_node.key:
                if main_node.right_node is not None:
                    main_node = main_node.right_node
                else:
                    main_node.right_node = new_node
                    new_node.parent_node = main_node
                    break
            else:
                self._splaying_process(main_node)
                print('error')
                return

        self._splaying_process(new_node)

    def set_by_key(self, key, value):
        if self.__root_node is None:
            print('error')
        else:
            searched_node = self._search_node(key)
            if searched_node is None:
                print('error')
            else:
                searched_node.value = value

    def min_node(self):
        if self.__root_node is None:
            print('error')
            return
        searched_node = self.__root_node.search_min_node()
        print(f"{searched_node.key} {searched_node.value}")
        self._splaying_process(searched_node)

    def max_node(self):
        if self.__root_node is None:
            print('error')
            return
        searched_node = self.__root_node.search_max_node()
        print(f"{searched_node.key} {searched_node.value}")
        self._splaying_process(searched_node)

    def search_by_key(self, key):
        if self.__root_node is None:
            print('0')
            return
        searched_node = self._search_node(key)
        if searched_node is None:
            print('0')
        else:
            print('1 ' + str(searched_node.value))

    def print(self, one_line=None):
        if self.__root_node is None:
            print('_')
            return
        if one_line is None:
            one_line = [self.__root_node]
        string = ''
        new_one_line = list()
        for node in one_line:
            if node is not None:
                if node.parent_node is None:
                    string += f'[{node.key} {node.value}] '
                else:
                    string += f'[{node.key} {node.value} {node.parent_node.key}] '
                new_one_line += [node.left_node, node.right_node]
            else:
                string += '_ '
                new_one_line += [None, None]

        if ']' in string:
            print(string[:-1])
            self.print(new_one_line)

    def delete_by_key(self, key):
        if self.__root_node is None:
            print('error')
            return
        deleted_node = self._search_node(key)
        if not deleted_node:
            print('error')
            return
        if not deleted_node.parent_node and not deleted_node.left_node and not deleted_node.right_node:
            self.__root_node = None
        elif not deleted_node.left_node:
            deleted_node.right_node.parent_node = None
            self.__root_node = deleted_node.right_node
        elif not deleted_node.right_node:
            deleted_node.left_node.parent_node = None
            self.__root_node = deleted_node.left_node
        else:
            right_of_deleted_node = deleted_node.right_node
            right_of_deleted_node.parent_node = self.__root_node
            new_root = deleted_node.left_node.search_max_node()
            self._splaying_process(new_root)
            new_root.parent_node = None
            new_root.right_node = right_of_deleted_node
            right_of_deleted_node.parent_node = new_root

    def _splaying_process(self, new_root):
        def rotation_process(main_type, tree, rotation_node):
            if main_type == 'left':
                main_type = 'left_node'
                minor_type = 'right_node'
            else:
                minor_type = 'left_node'
                main_type = 'right_node'
            parent = rotation_node.__dict__[minor_type]
            rotation_node.__dict__[minor_type] = parent.__dict__[main_type]
            if parent.__dict__[main_type] is not None:
                parent.__dict__[main_type].parent_node = rotation_node
            parent.parent_node = rotation_node.parent_node
            if rotation_node.parent_node is None:
                tree.__root_node = parent
            elif rotation_node.parent_node.left_node == rotation_node:
                rotation_node.parent_node.left_node = parent
            else:
                rotation_node.parent_node.right_node = parent
            rotation_node.parent_node = parent
            parent.__dict__[main_type] = rotation_node

        while new_root.parent_node is not None:
            if new_root.parent_node.parent_node is None:
                if new_root.parent_node.left_node == new_root:
                    rotation_process('right', self, new_root.parent_node)
                else:
                    rotation_process('left', self, new_root.parent_node)
            elif new_root.parent_node.left_node != new_root:
                if new_root.parent_node.parent_node.left_node == new_root.parent_node:
                    rotation_process('left', self, new_root.parent_node)
                    rotation_process('right', self, new_root.parent_node)
                else:
                    rotation_process('left', self, new_root.parent_node.parent_node)
                    rotation_process('left', self, new_root.parent_node)
            elif new_root.parent_node.left_node == new_root:
                if new_root.parent_node.parent_node.left_node == new_root.parent_node:
                    rotation_process('right', self, new_root.parent_node.parent_node)
                    rotation_process('right', self, new_root.parent_node)
                else:
                    rotation_process('right', self, new_root.parent_node)
                    rotation_process('left', self, new_root.parent_node)

    def _search_node(self, key):
        parent = None
        node = self.__root_node
        while True:
            if node is None:
                self._splaying_process(parent)
                return
            elif node.key > key:
                parent = node
                node = node.left_node
            elif node.key < key:
                parent = node
                node = node.right_node
            elif node.key == key:
                self._splaying_process(node)
                return node


splay_tree = SplayTree()

for line in stdin:
    line = line.replace('\n', '')

    if line == 'print':
        splay_tree.print()
    elif line == 'min':
        splay_tree.min_node()
    elif line == 'max':
        splay_tree.max_node()
    elif line[:6] == 'delete':
        key = int(line[7:])
        splay_tree.delete_by_key(key)
    elif line[:6] == "search":
        key = int(line[7:])
        splay_tree.search_by_key(key)
    elif line[:3] == 'set':
        items = line[4:].split(' ')
        key = int(items[0])
        value = items[1]
        splay_tree.set_by_key(key, value)
    elif line[:3] == 'add':
        items = line[4:].split(' ')
        key = int(items[0])
        value = items[1]
        splay_tree.add(key, value)
    elif len(line) > 1:
        print('error')
