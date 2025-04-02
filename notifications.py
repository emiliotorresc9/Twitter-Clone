from queue_e import QueueE


class NotificationManager:
    """
    Clase para manejar notificaciones usando una cola personalizada.
    """
    def __init__(self):
        self.notifications = QueueE()

    def add_notification(self, message):
        """
        Agrega una nueva notificación.
        """
        self.notifications.enqueue(message)

    def get_notifications(self):
        """
        Devuelve todas las notificaciones y las elimina de la cola.
        """
        all_notifications = []
        while not self.notifications.empty():
            all_notifications.append(self.notifications.dequeue())
        return all_notifications

    def has_notifications(self):
        """
        Verifica si hay notificaciones en la cola.
        """
        return not self.notifications.empty()

    def peek_notification(self):
        """
        Muestra la próxima notificación sin eliminarla.
        """
        if self.notifications.empty():
            return None
        return self.notifications.peek()

    def __repr__(self):
        """
        Representación en texto del administrador de notificaciones.
        """
        return repr(self.notifications)


# === Pruebas del NotificationManager ===
if __name__ == "__main__":
    notification_manager = NotificationManager()

    # Agregar notificaciones
    notification_manager.add_notification("User1 le dio like a tu publicación.")
    notification_manager.add_notification("User2 comenzó a seguirte.")
    notification_manager.add_notification("Nueva publicación de User3.")

    # Verificar notificaciones
    print("Notificaciones actuales:")
    print(notification_manager)

    # Obtener todas las notificaciones
    print("\nMostrando notificaciones:")
    notifications = notification_manager.get_notifications()
    for notif in notifications:
        print(notif)

    # Verificar si quedan notificaciones
    print("\n¿Hay notificaciones restantes?")
    print(notification_manager.has_notifications())
