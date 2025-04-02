import random
import string


class Member:
    """
    Clase que representa a un miembro en la red social.
    """
    def __init__(self, alias, last_name, name):
        """
        Inicializa un miembro con alias, apellido, nombre y una lista de amigos.
        """
        self.alias = alias
        self.last_name = last_name
        self.name = name
        self.friends = set()  # Conjunto para manejar amigos sin duplicados

    def make_friend(self, alias):
        """
        Agrega un alias al conjunto de amigos del usuario.
        """
        if alias != self.alias:  # Evitar agregar el propio alias
            self.friends.add(alias)

    def remove_friend(self, alias):
        """
        Elimina un alias del conjunto de amigos.
        """
        self.friends.discard(alias)  # Usa `discard` para evitar errores si el alias no existe

    def get_friends_list(self):
        """
        Devuelve una lista de amigos del usuario.
        """
        return list(self.friends)

    def __repr__(self):
        """
        Representación en texto del miembro.
        """
        return f"{self.name} {self.last_name} (@{self.alias})"


class UserManager:
    """
    Clase para gestionar usuarios.
    """
    def __init__(self):
        self.users = {}  # Diccionario para almacenar usuarios con alias como clave

    def register_user(self, alias, name):
        """
        Registra un nuevo usuario.
        """
        if alias not in self.users:
            last_name, first_name = name.split(" ", 1)
            self.users[alias] = Member(alias, last_name, first_name)

    def get_user(self, alias):
        """
        Obtiene un usuario por su alias.
        """
        return self.users.get(alias)

    def list_users(self):
        """
        Devuelve una lista de objetos `Member`.
        """
        return list(self.users.values())

    def list_aliases(self):
        """
        Devuelve una lista de alias de los usuarios registrados.
        """
        return list(self.users.keys())


# === Generadores de Alias y Nombres ===
def alias_generator():
    """
    Genera un alias único en el formato 'nombre_apellido_caracteres_emoji'.
    """
    names = [
        'John', 'Emma', 'Michael', 'Olivia', 'William', 'Sophia', 'James', 'Ava',
        'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Charlotte', 'Alexander', 
        'Amelia', 'Jackson', 'Harper', 'Ethan', 'Evelyn'
    ]
    last_names = [
        'Smith', 'Johnson', 'Brown', 'Williams', 'Jones', 'Garcia', 'Miller', 
        'Davis', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 
        'Moore', 'Martin', 'Jackson', 'Thompson', 'White', 'Lee', 'Harris'
    ]
    emojis = ['😊', '🎮', '📚', '🎵', '🐱', '🍕', '✈️', '😎', '🥳', '🚀']

    # Seleccionar elementos aleatorios
    name = random.choice(names).lower()
    last_name = random.choice(last_names).lower()
    emoji = random.choice(emojis)

    # Generar una cadena aleatoria de 4 caracteres
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

    # Combinar los elementos para formar el alias
    alias = f"{name}_{last_name}_{random_chars} {emoji}"
    return alias


def name_generator():
    """
    Genera un nombre y apellido aleatorio.
    """
    names = [
        'John', 'Emma', 'Michael', 'Olivia', 'William', 'Sophia', 'James', 'Ava',
        'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Charlotte', 'Alexander', 
        'Amelia', 'Jackson', 'Harper', 'Ethan', 'Evelyn'
    ]
    last_names = [
        'Smith', 'Johnson', 'Brown', 'Williams', 'Jones', 'Garcia', 'Miller', 
        'Davis', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 
        'Moore', 'Martin', 'Jackson', 'Thompson', 'White', 'Lee', 'Harris'
    ]

    # Seleccionar nombre y apellido aleatorio
    return random.choice(last_names), random.choice(names)
