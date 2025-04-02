import datetime


class Post:
    """
    Clase que representa una publicación en la red social.
    """
    def __init__(self, author, content):
        self.author = author  # Alias del autor de la publicación
        self.content = content  # Contenido de la publicación
        self.likes = set()  # Conjunto para manejar "Me gusta"
        self.comments = []  # Lista para almacenar comentarios
        self.timestamp = datetime.datetime.now()  # Fecha y hora de creación

    def add_like(self, user_alias):
        """
        Agrega un "Me gusta" de un usuario.
        """
        self.likes.add(user_alias)

    def add_comment(self, user_alias, comment):
        """
        Agrega un comentario de un usuario.
        """
        self.comments.append((user_alias, comment))

    def __repr__(self):
        """
        Representación en texto de la publicación.
        """
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.author}: {self.content}"


class PostManager:
    """
    Clase para gestionar publicaciones.
    """
    def __init__(self):
        self.posts = []  # Lista para almacenar publicaciones

    def add_post(self, author, content):
        """
        Agrega una nueva publicación.
        """
        new_post = Post(author, content)
        self.posts.append(new_post)

    def list_posts(self):
        """
        Devuelve todas las publicaciones.
        """
        return self.posts

    def search_posts(self, keyword):
        """
        Busca publicaciones por una palabra clave.
        """
        return [post for post in self.posts if keyword.lower() in post.content.lower()]

    def like_post(self, post, user_alias):
        """
        Agrega un "Me gusta" a una publicación específica.
        """
        post.add_like(user_alias)
