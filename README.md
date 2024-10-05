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