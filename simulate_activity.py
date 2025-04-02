from users import UserManager, alias_generator, name_generator
from posts import PostManager
import random


def simulate_activity(user_manager, post_manager, num_users=20):
    """
    Genera usuarios iniciales y publicaciones, asegurando que cada usuario tenga un mensaje único.
    """
    predefined_posts = [
        "Having pizza with family tonight 😋🍕",
        "Excited about the weekend! 🎉",
        "Workout complete! Feeling strong 💪",
        "Dreaming of travel ✈️🌍",
        "Coffee time ☕ and coding 💻",
        "Nature walk this morning 🌲☀️",
        "Just finished a great book 📚",
        "Relaxing with a good movie 🎬🍿",
        "Weekend road trip plans 🚗🗺️",
        "Happy to reconnect with old friends 😊",
        "Exploring a new city 🏙️🚶‍♂️",
        "Gardening and loving the sunshine 🌻☀️",
        "Learning new skills online 📖💻",
        "Celebrating a special day 🎂🥳",
        "Taking time to meditate and relax 🧘‍♂️🌿",
        "Cooking something delicious 🍳🍲",
        "Enjoying quality time with family 🏠❤️",
        "Back to work after a refreshing weekend 💼☕",
        "Watching my favorite series 📺🍿",
        "Planning a future adventure ✈️🌏",
    ]

    # Validar que haya suficientes mensajes para el número de usuarios
    if num_users > len(predefined_posts):
        raise ValueError("El número de usuarios no puede exceder el número de mensajes disponibles.")

    # Mezclar mensajes para asignarlos de forma aleatoria
    random.shuffle(predefined_posts)

    for i in range(num_users):
        # Generar alias y nombre aleatorios
        alias = alias_generator()
        last_name, name = name_generator()
        full_name = f"{name} {last_name}"

        # Registrar usuario
        user_manager.register_user(alias, full_name)

        # Asignar un mensaje único al usuario
        content = predefined_posts.pop()  # Extraer un mensaje único
        post_manager.add_post(alias, content)

        # Asignar un número aleatorio de likes a la publicación
        post = post_manager.list_posts()[-1]  # Obtener la última publicación
        num_likes = random.randint(0, 2000)

        # Agregar "Me gusta" simulados
        for _ in range(num_likes):
            liker_alias = alias_generator()  # Simular alias de los que dan "Me gusta"
            post.add_like(liker_alias)

        # Asignar un número aleatorio de comentarios entre 0 y 30
        num_comments = random.randint(0, 30)
        for _ in range(num_comments):
            commenter_alias = alias_generator()  # Simular alias de los que comentan
            comment = f"Comentario de {commenter_alias}"  # Generar un comentario genérico
            post.add_comment(commenter_alias, comment)

    print(f"{num_users} usuarios y publicaciones iniciales generados exitosamente.")


if __name__ == "__main__":
    # Crear instancias de UserManager y PostManager
    user_manager = UserManager()
    post_manager = PostManager()

    # Generar usuarios y publicaciones iniciales
    simulate_activity(user_manager, post_manager)

    # Imprimir usuarios registrados
    print("Usuarios registrados:")
    for user in user_manager.list_users():
        print(user)

    # Imprimir publicaciones iniciales
    print("\nPublicaciones iniciales:")
    for post in post_manager.list_posts():
        print(f"{post.author}: {post.content} | Likes: {len(post.likes)} | Comentarios: {len(post.comments)}")
