class FriendManager:
    def __init__(self):
        """
        Inicializa un conjunto vacío para almacenar los amigos.
        """
        self.friends = set()

    def add_friend(self, alias):
        """
        Agrega un alias al conjunto de amigos.
        """
        if alias in self.friends:
            return f"{alias} ya es tu amigo."
        else:
            self.friends.add(alias)
            return f"Has agregado a {alias} como amigo."

    def get_friends(self):
        """
        Devuelve una lista de amigos actuales.
        """
        if not self.friends:
            return "No tienes amigos aún."
        return "\n".join(self.friends)
