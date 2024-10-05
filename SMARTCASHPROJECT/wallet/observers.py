from abc import ABC, abstractmethod

# Subject interface
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass

# Concrete observer for goals
class GoalCreatedObserver(Observer):
    def update(self, event):
        print(f"Notificación: Se ha creado/modificado una meta: {event}")
        # Aquí se podrá implementar más lógica en un futuro, como enviar un correo electrónico o registrar el evento.
