class QueueE:
    """
    Implementación personalizada de una cola.
    """
    def __init__(self):
        self.lista = []

    def enqueue(self, data):
        """
        Agrega un elemento al final de la cola.
        """
        self.lista.append(data)

    def dequeue(self):
        """
        Elimina y devuelve el primer elemento de la cola.
        """
        if self.empty():
            raise IndexError("dequeue from empty queue")
        return self.lista.pop(0)

    def empty(self):
        """
        Verifica si la cola está vacía.
        """
        return len(self.lista) == 0

    def peek(self):
        """
        Devuelve el primer elemento sin eliminarlo.
        """
        if self.empty():
            raise IndexError("peek from empty queue")
        return self.lista[0]

    def size(self):
        """
        Devuelve el tamaño de la cola.
        """
        return len(self.lista)

    def __repr__(self):
        """
        Representación en cadena de la cola.
        """
        return f"QueueE({self.lista})"


if __name__ == "__main__":
    # Pruebas de la cola personalizada
    queue = QueueE()
    queue.enqueue("Notificación 1")
    queue.enqueue("Notificación 2")
    queue.enqueue("Notificación 3")
    print("Cola actual:", queue)
    print("Primer elemento:", queue.peek())
    print("Eliminando elemento:", queue.dequeue())
    print("Cola después de dequeue:", queue)
