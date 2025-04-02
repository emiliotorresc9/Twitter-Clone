class Node:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class HeapPQueue:
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, priority, data):
        new_node = Node(priority, data)

        if not self.root:
            self.root = new_node
        else:
            self.__insert_node(new_node)
            self.__bubble_up(new_node)

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        max_node = self.root
        priority, data = max_node.priority, max_node.data

        if self.size == 1:
            self.root = None
        else:
            last_node = self.__get_last_node()
            self.__swap(max_node, last_node)
            self.__remove_last_node()
            self.__bubble_down(self.root)

        self.size -= 1

        return priority, data


    def peek(self):
        """
        Devuelve el nodo con la máxima prioridad sin eliminarlo.
        """
        if not self.root:
            raise IndexError("peek from empty queue")
        return self.root.priority, self.root.data

    def __insert_node(self, new_node):
        """
        Inserta un nodo en la posición correcta dentro del heap.
        """
        path = bin(self.size + 1)[3:]
        current = self.root
        parent = None

        for direction in path:
            parent = current
            current = current.left if direction == "0" else current.right

        new_node.parent = parent
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node

    def __bubble_up(self, node):
        """
        Ajusta la posición del nodo hacia arriba para mantener la propiedad del heap.
        """
        while node.parent and node.priority > node.parent.priority:
            self.__swap(node, node.parent)
            node = node.parent

    def __bubble_down(self, node):
        """
        Ajusta la posición del nodo hacia abajo para mantener la propiedad del heap.
        """
        while node.left:
            larger_child = node.left

            if node.right and node.right.priority > node.left.priority:
                larger_child = node.right

            if node.priority < larger_child.priority:
                self.__swap(node, larger_child)
            else:
                break

    def __get_last_node(self):
        """
        Obtiene el último nodo del heap.
        """
        path = bin(self.size)[3:]
        current = self.root

        for direction in path:
            current = current.left if direction == "0" else current.right

        return current

    def __remove_last_node(self):
        """
        Elimina el último nodo del heap.
        """
        path = bin(self.size)[3:]
        current = self.root
        parent = None

        for direction in path:
            parent = current
            current = current.left if direction == "0" else current.right

        if parent.left == current:
            parent.left = None
        else:
            parent.right = None

    def __swap(self, node1, node2):
        """
        Intercambia los valores de dos nodos.
        """
        node1.priority, node2.priority = node2.priority, node1.priority
        node1.data, node2.data = node2.data, node1.data

    def print_heap(self, node, level=0):
        """
        Imprime el heap de forma jerárquica.
        """
        if node:
            self.print_heap(node.right, level + 1)
            print("       " * level + f"({node.priority}, {node.data})")
            self.print_heap(node.left, level + 1)
