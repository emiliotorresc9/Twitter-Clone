import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from users import UserManager
from posts import PostManager
from notifications import NotificationManager
from simulate_activity import simulate_activity
from heap_queue import HeapPQueue
from friend_manager import FriendManager
from search import bmh_search  

class TwitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitter Clone")
        self.root.geometry("700x700")
        self.root.configure(bg="lightblue")

        # Instancias de UserManager, PostManager, NotificationManager y FriendManager
        self.user_manager = UserManager()
        self.post_manager = PostManager()
        self.notification_manager = NotificationManager()
        self.priority_queue = HeapPQueue()
        self.friend_manager = FriendManager()

        # Generar usuarios, publicaciones iniciales y notificaciones simuladas
        simulate_activity(self.user_manager, self.post_manager)
        self.simulate_notifications()

        # Configuración de la interfaz
        self.setup_interface()

    def setup_interface(self):
        """
        Configura la interfaz principal.
        """
        # Lado Izquierdo (Botones y Logo)
        left_frame = tk.Frame(self.root, bg="lightblue", width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Logo y título
        try:
            logo = tk.PhotoImage(file="twitter_logo.png")
            logo_label = tk.Label(left_frame, image=logo, bg="lightblue")
            logo_label.image = logo  # Mantener referencia para evitar que se borre
            logo_label.pack(pady=20)
        except Exception as e:
            print(f"Error al cargar el logo: {e}")

        tk.Label(left_frame, text="Twitter Clone", font=("Helvetica", 24, "bold"), bg="lightblue").pack(pady=10)

        # Botones
        self.create_buttons(left_frame)

        # Lado Derecho (Publicaciones)
        self.create_posts_area()

        # Mostrar publicaciones iniciales
        self.display_posts(self.post_manager.list_posts())

    def create_buttons(self, parent):
        """
        Crea los botones principales de la aplicación.
        """
        tk.Button(parent, text="Ver Destacados", command=self.show_top_posts, width=25).pack(pady=10)
        tk.Button(parent, text="Ver Todas las Publicaciones", command=self.list_posts, width=25).pack(pady=10)
        tk.Button(parent, text="Agregar Publicación", command=self.add_post, width=25).pack(pady=10)
        tk.Button(parent, text="Ver Amigos", command=self.view_friends, width=25).pack(pady=10)
        tk.Button(parent, text="Ver Notificaciones", command=self.view_notifications, width=25).pack(pady=10)
        tk.Button(parent, text="Buscar", command=self.search, width=25).pack(pady=10)

    def create_posts_area(self):
        """
        Configura el área de publicaciones con un canvas scrollable.
        """
        self.posts_frame = tk.Frame(self.root, bg="white")
        self.posts_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.posts_canvas = tk.Canvas(self.posts_frame, bg="white", highlightthickness=0)
        self.posts_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.posts_frame, orient="vertical", command=self.posts_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.posts_canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas_frame = tk.Frame(self.posts_canvas, bg="white")
        self.posts_canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

        self.canvas_frame.bind("<Configure>", lambda e: self.posts_canvas.configure(scrollregion=self.posts_canvas.bbox("all")))

    def refresh_posts(self, posts):
        """
        Refresca el área de publicaciones con contenido nuevo.
        """
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        for post in posts:
            post_frame = tk.Frame(self.canvas_frame, bg="lightgrey", relief=tk.RIDGE, bd=2)
            post_frame.pack(fill=tk.X, padx=20, pady=15)

            # Información del post
            tk.Label(post_frame, text=f"Autor: {post.author}", font=("Arial", 14, "bold"), bg="lightgrey").pack(anchor="w", pady=5)
            tk.Label(post_frame, text=post.content, bg="lightgrey", wraplength=900, font=("Arial", 16)).pack(anchor="w", pady=5)
            tk.Label(post_frame, text=f"Likes: {len(post.likes)} | Comentarios: {len(post.comments)}", bg="lightgrey", font=("Arial", 12)).pack(anchor="w", pady=5)

            # Contenedor para el botón en la parte inferior derecha
            button_frame = tk.Frame(post_frame, bg="lightgrey")
            button_frame.pack(fill=tk.BOTH, pady=5)
            tk.Button(button_frame, text="Añadir Amigo", command=lambda alias=post.author: self.add_friend(alias), bg="white", font=("Arial", 12)).pack(side=tk.RIGHT, padx=10)
            
            # Botón de "Me gusta"
            tk.Button(button_frame, text="Me gusta", command=lambda p=post: self.like_post(p), bg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

    def display_posts(self, posts):
        """
        Muestra las publicaciones en el área.
        """
        self.refresh_posts(posts)

    def simulate_notifications(self):
        """
        Simula notificaciones iniciales.
        """
        users = self.user_manager.list_users()
        for user in users:
            alias = user.alias
            message = f"{alias} ha publicado algo nuevo."
            self.notification_manager.add_notification(message)

    def view_notifications(self):
        """
        Muestra las notificaciones pendientes al usuario.
        """
        notifications = self.notification_manager.get_notifications()
        if notifications:
            messagebox.showinfo("Notificaciones", "\n".join(notifications))
        else:
            messagebox.showinfo("Notificaciones", "No tienes notificaciones nuevas.")

    def show_top_posts(self):
        """
        Muestra las publicaciones destacadas ordenadas por número de 'Me gusta'.
        """
        # Obtener todas las publicaciones y ordenarlas por el número de "likes"
        top_posts = sorted(self.post_manager.list_posts(), key=lambda post: len(post.likes), reverse=True)[:10]
        self.display_posts(top_posts)

    def list_posts(self):
        """
        Muestra todas las publicaciones.
        """
        self.display_posts(self.post_manager.list_posts())

    def add_post(self):
        """
        Crea una nueva publicación.
        """
        alias = tk.simpledialog.askstring("Agregar Publicación", "Ingresa tu alias:")
        content = tk.simpledialog.askstring("Agregar Publicación", "Escribe tu publicación:")
        if alias and content:
            self.post_manager.add_post(alias, content)
            # Mostrar la nueva publicación al principio
            new_post = self.post_manager.list_posts()[-1]
            self.display_posts([new_post] + self.post_manager.list_posts()[:-1])

    def add_friend(self, alias):
        """
        Agrega un amigo a la lista de amigos del usuario.
        """
        message = self.friend_manager.add_friend(alias)
        messagebox.showinfo("Amigos", message)

    def view_friends(self):
        """
        Muestra la lista de amigos del usuario.
        """
        friends = self.friend_manager.get_friends()
        messagebox.showinfo("Amigos", f"Tus amigos:\n{friends}")

    def like_post(self, post):
        """
        Maneja el evento de hacer clic en "Me gusta" y actualiza el contador de likes.
        """
        # Se simula que un usuario da "Me gusta" con un alias aleatorio
        user_alias = tk.simpledialog.askstring("Me gusta", "Ingresa tu alias:")
        if user_alias:
            post.add_like(user_alias)  # Agrega el "Me gusta"
            self.display_posts(self.post_manager.list_posts())  # Refresca las publicaciones para mostrar el nuevo conteo de "Me gusta"

    def search(self):
        """
        Busca publicaciones o usuarios que coincidan con la palabra clave.
        """
        keyword = tk.simpledialog.askstring("Buscar", "Ingrese una palabra clave para buscar:")
        if not keyword:
            return

        # Buscar en publicaciones
        matching_posts = []
        for post in self.post_manager.list_posts():
            if bmh_search(post.content, keyword) != -1:
                matching_posts.append(post)

        # Buscar en usuarios
        matching_users = []
        for user in self.user_manager.list_users():
            if bmh_search(user.name, keyword) != -1 or bmh_search(user.alias, keyword) != -1:
                matching_users.append(user)

        # Mostrar resultados
        results = []
        if matching_users:
            results.append("Usuarios encontrados:")
            results.extend([f"{user.name} (@{user.alias})" for user in matching_users])
        else:
            results.append("No se encontraron usuarios.")

        if matching_posts:
            results.append("\nPublicaciones encontradas:")
            results.extend([f"{post.author}: {post.content}" for post in matching_posts])
        else:
            results.append("\nNo se encontraron publicaciones.")

        messagebox.showinfo("Resultados de la búsqueda", "\n".join(results))


if __name__ == "__main__":
    root = tk.Tk()
    app = TwitterApp(root)
    root.mainloop()
