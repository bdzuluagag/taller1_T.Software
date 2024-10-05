# SmartCash
## Proyecto Integrador 

### Para instalar lo necesario:
- pip install django
- pip install matplotlib
- pip install crispy-bootstrap5


### Comandos para iniciar:
Dentro de la carpeta SMARTCASHPROJECT/:
- python manage.py runserver


---

## Revisión Autocrítica de parámetro de calidad

### Usabilidad
- **Aspectos positivos**: La interfaz parece clara y fácil de navegar. El uso de vistas como `home`, `register` y `movements` hace que la estructura del sitio sea comprensible.
- **Aspectos a mejorar**: Sería beneficioso simplificar el proceso de interacción para el usuario, reduciendo la cantidad de campos obligatorios o pasos innecesarios.

### Compatibilidad
- **Aspectos positivos**: Utiliza el framework Django, lo cual garantiza compatibilidad con distintas bases de datos y sistemas operativos.
- **Aspectos a mejorar**: Se podría mejorar la compatibilidad incluyendo pruebas en más navegadores y dispositivos para asegurar la misma experiencia de usuario.

### Mantenibilidad
- **Aspectos positivos**: El código está segmentado en diferentes vistas, modelos y servicios, lo que facilita la lectura.
- **Aspectos a mejorar**: Se podrían implementar patrones de diseño para separar más claramente la lógica de negocio de la lógica de presentación, lo cual haría el proyecto más fácil de mantener.

### Rendimiento
- **Aspectos positivos**: Las consultas a la base de datos están segmentadas, lo que facilita la optimización.
- **Aspectos a mejorar**: Algunas consultas como `search_user_categories` se realizan varias veces sin optimización. Implementar caché o mejorar la eficiencia de estas consultas ayudaría al rendimiento.

### Seguridad
- **Aspectos positivos**: Utiliza el sistema de autenticación de Django, lo cual garantiza seguridad básica en el manejo de usuarios.
- **Aspectos a mejorar**: Las funcionalidades deberían ser evaluadas con un enfoque más fuerte en la validación de entradas y la protección contra ataques como CSRF.

---

## Inversión de Dependencias en la Vista de Movimientos

### ¿Por qué aplicamos la inversión de dependencias?

En este proyecto, aplicamos la inversión de dependencias para hacer que la vista `movements` sea más modular y flexible. Inicialmente, la vista dependía directamente de funciones específicas del módulo `movements` para leer movimientos financieros y generar archivos CSV. Esto puede dificultar la mantenibilidad del código, ya que cualquier cambio en las operaciones de movimientos impactaría directamente en la vista.

Para resolver este problema, extraímos la lógica relacionada con los movimientos a una clase independiente llamada `MovementService`. Esto tiene varias ventajas:

- **Modularidad**: Ahora la vista no depende directamente de la lógica de los movimientos, lo que facilita cambiar o extender la funcionalidad sin modificar la vista.
- **Reutilización**: El servicio puede ser reutilizado en otras partes del proyecto si se necesita trabajar con movimientos financieros.
- **Facilidad de pruebas**: La vista se puede probar de manera aislada, sin preocuparse por los detalles de la implementación de movimientos, lo que mejora la capacidad de hacer tests unitarios.

### ¿Cómo se implementó?

1. **Creación del servicio de movimientos**:
   Se creó una nueva clase llamada `MovementService` en el archivo `services.py`. Esta clase encapsula toda la lógica relacionada con los movimientos financieros de un usuario, como la lectura de movimientos y la generación de archivos CSV.

   ```python
   # services.py
   class MovementService:
       def __init__(self, user):
           self.user = user

       def get_user_movements(self, incomes, exits):
           # Lógica para leer los movimientos del usuario
           return mov.read_movements(incomes, exits, self.user)

       def generate_movements_csv(self, user_movements):
           # Lógica para generar el archivo CSV con los movimientos
           mov.generate_movements_csv(user_movements, self.user)
           # Código para devolver el archivo CSV como respuesta HTTP
   ```

2. **Modificación de la vista `movements`**:
   La vista fue modificada para inyectar una instancia de `MovementService`, en lugar de depender directamente de las funciones del módulo `mov`. De esta forma, la vista ahora interactúa con los movimientos financieros a través del servicio.

   ```python
   # views.py
   def movements(request):
       # Inyección del servicio de movimientos
       movement_service = MovementService(request.user)

       # Lógica de la vista, delegando las operaciones al servicio
       user_movements = movement_service.get_user_movements(incomes, exits)
       if download_movements == '':
           return movement_service.generate_movements_csv(user_movements)

   ```

### Beneficios de esta implementación:

- **Mantenibilidad**: Cualquier cambio en la lógica de movimientos ahora puede realizarse en el servicio, sin necesidad de modificar la vista.
- **Flexibilidad**: Podemos cambiar la implementación de `MovementService` (por ejemplo, usando una fuente de datos diferente) sin afectar la vista.
- **Testabilidad**: La vista ahora depende de una abstracción, por lo que es fácil simular el comportamiento del servicio en pruebas unitarias.

Con este cambio, se ha implementado una inversión de dependencias en la vista de movimientos, haciendo que el código sea más modular, mantenible y fácil de probar.

---

## Implementación del patrón de diseño Observer de Python en la funcionalidad de creación de metas

### ¿Por qué aplicamos el Patrón Observer?
El **patrón Observer** se implementó en la funcionalidad de creación de metas para agregar una mejora en la notificación de eventos. Este patrón es adecuado porque la creación de una meta puede ser relevante para varios componentes del sistema, y el patrón Observer permite notificar automáticamente a otros módulos cuando se produce este evento, sin acoplar directamente las dependencias.

Este patrón es ideal para situaciones donde múltiples objetos necesitan reaccionar a un cambio en el estado de otro objeto, que es justamente el caso de la funcionalidad de metas. Implementar Observer permite mantener un diseño desacoplado, mejorando la escalabilidad del sistema.

### ¿Cómo se implementó?
1. **Creación de `observers.py`**: Se creó el archivo `observers.py` en la carpeta `wallet`. En este archivo, se implementó el patrón Observer, que consiste en:
   - La clase `GoalSubject` para gestionar la suscripción y notificación de los observadores.
   - La clase `GoalCreatedObserver` como observador para recibir notificaciones sobre la creación o modificación de una meta.
  
     ```python
     # observers.py
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
      ```

2. **Actualización de la Vista de Metas (`views.py`)**:
   - En la función `goals()`, se añadió lógica para instanciar el sujeto (`GoalSubject`) y registrar un observador (`GoalCreatedObserver`).
   - Cada vez que se crea una meta, se notifica al observador registrado.

   ```python
   # views.py
   def goals(request):
    connection.current_user = request.user

    # Creación del sujeto
    goal_subject = Subject()
    # Añadir el observador
    goal_observer = GoalCreatedObserver()
    goal_subject.add_observer(goal_observer)

    goal_name = request.GET.get('goal_name')
    goal_value = request.GET.get('goal_value')
    goal_date = request.GET.get('goal_date')

    if goal_date and goal_name and goal_value:
        connection.create_goal(goal_name.lower(), goal_value, goal_date, request.user)
        connection.create_category(goal_name, request.user)

        # Notificar a los observadores sobre la nueva meta
        goal_subject.notify_observers(f"Meta '{goal_name}' creada con valor {goal_value} y fecha {goal_date}")

    user_goals = connection.search_user_goals(request.user)
    user_estimated_dates = mov.date_estimated(user_goals)

    return render(request, 'registration/goals.html',
                  {'goal_name': goal_name, 'goal_value': goal_value, 'goal_date': goal_date, 'user_goals': user_goals, 'estimated_dates': user_estimated_dates})
   ```
3. **Mensajes de Consola**: Para comprobar la correcta notificación, se añadió un `print()` en `GoalCreatedObserver` que imprime un mensaje cuando se crea o modifica una meta.

   ```python
   # observers.py
   class GoalCreatedObserver(Observer):
    def update(self, event):
        print(f"Notificación: Se ha creado/modificado una meta: {event}")
   ```

### Beneficios de esta implementación:
1. **Desacoplamiento**: La vista de metas no necesita saber qué hacer con las acciones posteriores a la creación de una meta. El patrón Observer maneja estas acciones automáticamente, facilitando el mantenimiento y la modificación de la funcionalidad.

2. **Escalabilidad**: Si en el futuro se requieren más acciones al crear o modificar una meta (por ejemplo, enviar un correo electrónico o registrar un log), se puede simplemente agregar más observadores al sujeto, sin modificar el código de la vista.

3. **Reutilización de Código**: La lógica del observador puede ser reutilizada en otras partes del sistema si surgen eventos similares, lo cual facilita la expansión del sistema con un mínimo esfuerzo de desarrollo adicional.
 
Estos cambios permiten que el sistema reaccione de manera más flexible y desacoplada ante eventos importantes, mejorando su mantenimiento y escalabilidad.

---

## Implementación del patrón de diseño de Normalización de Modelo para la Tercera Forma Normal (NF3)

### ¿Por qué aplicamos la Normalización de Modelo?
La normalización de modelo se implementó para estructurar la base de datos de manera que se minimice la redundancia de datos y se eliminen las dependencias no deseadas. La Tercera Forma Normal (NF3) es crucial para garantizar que cada campo en una tabla sea dependiente solo de la clave primaria. Al hacerlo, se mejora la integridad de los datos y se facilita la mantenibilidad y escalabilidad del sistema.

Este patrón es ideal para aplicaciones donde los datos están interrelacionados y pueden ser propensos a cambios. Implementar NF3 ayuda a garantizar que las modificaciones en los datos se reflejen adecuadamente sin provocar inconsistencias.

## ¿Cómo se implementó?
### Identificación de Entidades y Relaciones:

- Se identificaron las entidades clave del modelo de datos, como Usuario, Meta, Movimiento y Categoría.
- Se definieron las relaciones entre estas entidades, asegurando que cada entidad estuviera relacionada de manera lógica y que las dependencias estuvieran claras.

### Creación de Tablas Normalizadas:

Se crearon las tablas de base de datos siguiendo las reglas de la NF3. Esto implica que:
- Cada tabla tiene una clave primaria única.
- No hay dependencias transitivas; los atributos de cada tabla dependen únicamente de la clave primaria.
- Se eliminaron las columnas que no dependían directamente de la clave primaria.

Uno de los ejemplos de este cambio fue con la clase movimiento que fue actualizada:

#### Versión Antigua
```python
    # models.py
    class Movimiento(models.Model):
        nombre = models.CharField(max_length=100)
        usuario = models.ForeignKey(User, on_delete=models.CASCADE)
        direccion = models.CharField(max_length=10)
        valor = models.IntegerField()
        fecha = models.DateField()
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)      
        def __str__(self):
            return f'{self.usuario.__str__()} - {self.nombre}'
```

#### Nueva Versión
```python
    # models.py
    class Movimiento(models.Model):
        nombre = models.CharField(max_length=100) # Se eliminó el field usuario
        direccion = models.CharField(max_length=10)
        valor = models.IntegerField()
        fecha = models.DateField()
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

        def __str__(self):
            return f'{self.categoria.usuario.__str__()} - {self.nombre}'
```

### Implementación de Consultas y Operaciones:

- Se implementaron las operaciones CRUD (Crear, Leer, Actualizar y Borrar) de manera que las consultas fueran eficientes y que respetaran la estructura normalizada.
- Cada operación se diseñó para operar sobre las tablas de forma que se mantuviera la integridad referencial y se respetara la normalización.

### Beneficios de la Normalización a NF3

1. **Reducción de la Redundancia**: Se minimizan los datos duplicados, lo que ahorra espacio y reduce la posibilidad de inconsistencias.

2. **Mejor Integridad de los Datos**: Al eliminar dependencias no deseadas, se asegura que los datos sean más confiables y fáciles de mantener.

3. **Escalabilidad**: La estructura normalizada permite agregar nuevas funcionalidades y relaciones sin afectar la integridad del sistema.
Implementar la normalización a NF3 en el modelo de datos no solo mejora la estructura de la base de datos, sino que también sienta las bases para un desarrollo futuro más limpio y eficiente.