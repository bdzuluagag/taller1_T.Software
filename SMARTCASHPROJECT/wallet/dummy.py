from .models import Movimiento, Categoria
import random
from django.contrib.auth.models import User
from datetime import date
nombres = [
    "Sofía", "Mateo", "Valentina", "Santiago", "Isabella", "Matías", "Emma", "Benjamín", "Mariana", "Lucas",
    "Camila", "Sebastián", "Victoria", "Dylan", "Valeria", "Martín", "Daniela", "Joaquín", "Lucía", "Emilio",
    "Ximena", "Samuel", "Gabriela", "Gabriel", "Amanda", "Diego", "Luisa", "Nicolás", "Alejandra", "Oliver",
    "Fernanda", "Daniel", "Jimena", "Miguel", "Sara", "David", "Emily", "Samuel", "Abril", "Ángel",
    "Alessandra", "Adrián", "Paula", "Vicente", "Renata", "Carlos", "Isabel", "Juan", "Carolina", "Mariano",
    "Aitana", "Andrés", "Guadalupe", "Federico", "Rosa", "Javier", "Alma", "Luciano", "Clara", "Leonardo",
    "Ana", "Eduardo", "Julia", "Raúl", "Laura", "Pablo", "Bianca", "Óscar", "Catalina", "Enrique",
    "Celeste", "Hugo", "Alexa", "Iker", "Regina", "Felipe", "Mía", "Álvaro", "Renata", "Rodrigo",
    "Paulina", "José", "María", "Agustín", "Luna", "Lorenzo", "Paulina", "Emmanuel", "Alejandra", "Ignacio",
    "Elena", "Alexis", "Melissa", "Diego", "Gabriela", "Francisco", "Ingrid", "Mario", "Denisse", "Alberto",
    "Ángela", "Cristian", "Montserrat", "Sergio", "Patricia", "Mauricio", "Florencia", "Armando", "Antonella",
    "Roberto",
    "Esmeralda", "Jorge", "Natalia", "Luis", "Susana", "Gonzalo", "Estefanía", "Edgar", "Rocío", "Jaime",
    "Beatriz", "Ernesto", "Julieta", "Víctor", "Xiomara", "René", "Maya", "Salvador", "Ana Sofía", "Óliver",
    "Abril", "Jesús", "Elizabeth", "Mauricio", "Daniela", "Ángel", "Fernanda", "Felipe", "Gabriela", "Andrés",
    "Valentina", "Alejandro", "María José", "César", "Karen", "Julio", "Carla", "Adrián", "Jimena", "Juan Pablo",
    "Alondra", "Julián", "Valery", "Gerardo", "Ivanna", "Maximiliano", "Danna", "Alonso", "Miranda", "Marco",
    "Estefanía", "Lorenzo", "Ana Laura", "Emilio", "Sofía", "Axel", "Adriana", "Cristóbal", "Verónica", "Rodolfo",
    "Samantha", "Pedro", "Alessandra", "Emanuel", "Stephanie", "Alan", "Patricia", "Nicolás", "Dulce", "Eduardo",
    "Brenda", "Álvaro", "Leslie", "Edwin", "Ximena", "Armando", "Karen", "Héctor", "Berenice", "Javier",
    "Valeria", "Leonel", "Susana", "Luis Ángel", "Nancy", "Ricardo", "Daniela", "Raúl", "Regina", "Francisco Javier",
    "Diana", "Rafael", "Jazmín", "Bryan", "Priscila", "Manuel", "Ana Paula", "Diego", "Mariana", "Ismael",
    "Fernanda", "Óscar", "Adriana", "Alejandro", "Dafne", "Josué", "Ariana", "Carlos Alberto", "Monserrat", "Hugo",
    "Karla", "Gerardo", "Montserrat", "Jorge", "Estefany", "Jesús", "Yareli", "Cristian", "Karina", "Joel",
    "Sandra", "Juan Carlos", "Gabriela", "Erick", "Claudia", "Alex", "María Fernanda", "Gilberto", "Brenda",
    "Luis Fernando", "Anahí", "Antonio", "Nataly", "Julio César", "Melanie", "Jaime", "Alejandra", "Arturo",
    "Bárbara", "Samuel", "Paola", "Víctor Manuel", "Lizeth", "Roberto", "Ileana", "Raúl", "Monica", "Simón",
    "Susana", "Cristóbal", "María", "Ramón", "Sara", "Gustavo", "Tania", "Rubén", "Claudia", "Rogelio",
    "Samantha", "Óscar", "Jocelyn", "Ignacio", "Verónica", "Damián", "Noelia", "Jaime", "Silvia", "Aarón",
    "Ximena", "Ángel", "Ana", "Adán", "Mayra", "Ariel", "Yolanda", "Isaac", "Karime", "Héctor",
    "Dulce María", "Miguel Ángel", "Roxana", "Joel", "Lorena", "Ulises", "Ale", "Salvador", "Irma", "Nicolás",
    "Yasmin", "Manuel", "Sandra", "Édgar", "Lidia", "Arturo", "Gloria", "Eduardo", "Georgina", "Sebastián",
    "Rosa María", "Rodrigo", "Leticia", "Aldo", "Maricela", "Jonathan", "Isis", "Fabián", "Cecilia", "Emanuel",
    "Raquel", "Braulio", "Fátima", "Maximiliano", "Paulette", "Mauricio", "Guillermina", "Mariano", "Carmen", "Yahir",
    "Esperanza", "Ángel"]

apellidos = [
    "García", "Rodríguez", "González", "López", "Martínez", "Hernández", "Pérez", "Sánchez", "Ramírez", "Torres",
    "Flores", "Rivera", "Gómez", "Díaz", "Reyes", "Morales", "Cruz", "Ortiz", "Silva", "Romero",
    "Vargas", "Ramos", "Castillo", "Fernández", "Gutiérrez", "Mendoza", "Castro", "Guzmán", "Ortega", "Chávez",
    "Mendoza", "Ruiz", "Jiménez", "Moreno", "Rojas", "Cortés", "Soto", "Rojas", "Herrera", "Aguilar",
    "Medina", "Núñez", "Campos", "Vega", "Delgado", "Santos", "Carrillo", "Guerrero", "Pacheco", "Paredes",
    "Palacios", "Castañeda", "Cabrera", "Cervantes", "Valdez", "Ponce", "Zúñiga", "Escobar", "Herrera", "Arias",
    "Navarro", "Andrade", "Cuevas", "Acosta", "Velasco", "Montes", "Sandoval", "Ríos", "Fuentes", "Vargas",
    "Esparza", "Rosales", "Benítez", "Salgado", "Córdova", "Miranda", "Zamora", "Escamilla", "Villanueva", "Vargas",
    "Solís", "Castañeda", "Trejo", "Olvera", "Zavala", "Valenzuela", "Lara", "Cordero", "Valdés", "Cabrera",
    "Guevara", "Cepeda", "Villarreal", "Cárdenas", "Urrutia", "Mora", "Ayala", "Esquivel", "Barrera", "Hurtado",
    "Lara", "Escalante", "Calderón", "Gallegos", "Galván", "Salazar", "Navarro", "Munguía", "Contreras", "Cárdenas",
    "Tapia", "Vallejo", "Cuevas", "Bautista", "Tovar", "Arellano", "Puga", "Landa", "Ríos", "Juárez",
    "Domínguez", "Ríos", "Sepúlveda", "Escudero", "Terrazas", "Aragón", "Merino", "Uribe", "Ávalos", "Pinto",
    "Barajas", "Barraza", "Arenas", "Beltrán", "Macías", "Camacho", "González", "Madrid", "Zaragoza", "Bravo",
    "Carreón", "Rueda", "Villegas", "Miramontes", "Rocha", "Camarillo", "Moya", "Vargas", "Paredes", "Hernández",
    "Quintero", "Escalera", "Barrios", "Osorio", "Del Río", "Barajas", "Llamas", "Campa", "Arellano", "Leyva",
    "Fuentes", "Rosas", "Rubio", "Figueroa", "Saucedo", "Córdoba", "Gámez", "Gastélum", "Vargas", "Miranda",
    "Jiménez", "Lomelí", "Ibarra", "Cota", "Ríos", "Elizondo", "Castañeda", "Padilla", "Segura", "Serna",
    "Grajeda", "Toledo", "Fregoso", "Godoy", "Galindo", "Palma", "Franco", "Salas", "Valle", "Figueroa",
    "Baños", "Becerra", "Villar", "Aguirre", "Valle", "Aguirre", "Navarro", "López", "Aguirre", "Quiroz",
    "Salazar", "Manríquez", "Vega", "Paredes", "Lemus", "Vargas", "Montaño", "Pacheco", "Becerra", "Román",
    "Moreno", "Treviño", "Serrano", "Godínez", "Carrasco", "Hinojosa", "Román", "Ibarra", "Vizcarra", "Del Toro",
    "Lima", "Solano", "Elías", "Esparza", "Gálvez", "Santana", "Páez", "Báez", "Ríos", "Anguiano",
    "Barajas", "Ortiz", "Hidalgo", "Villa", "Santoyo", "Nava", "Orozco", "Arroyo", "Brito", "Castellanos",
    "Valle", "Salcedo", "Monroy", "Vásquez", "Escudero", "Ayala", "Cedillo", "Aguilera", "Contreras", "Monge",
    "Muñoz", "Zamora", "Gómez", "Morales", "Lázaro", "Osuna", "Ferreira", "Madero", "Solano", "Bustamante",
    "León", "Ponce", "Vázquez", "Ferrari", "Belmonte", "Ávila", "Morales", "Rivero", "Mora", "Madrigal",
    "Santiago", "Estrada", "Villalpando", "Garay", "Dorantes", "Del Ángel", "Suárez", "Villanueva", "Aguilar", "Nava",
    "Márquez", "Leyva", "Zapata", "Báez", "Bernal", "Chávez", "Galván", "Becerra", "Gudiño", "Cerezo",
    "Montero", "Briseño", "Fierro", "De la Rosa", "Del Río", "Valverde", "Vallejo", "Garrido", "Avalos",
    "Guzmán", "Guerrero", "Villalobos", "Robledo", "Quintana", "Ríos", "Santos", "Guzmán", "Galván", "Barajas",
    "Báez", "Solís", "Rosales"]


def generate_dummy():
    for i in range(300):
        user = User(username=f'{nombres[i]}_{apellidos[i]}{random.randint(0, 100)}', email=f'{nombres[i]}{apellidos[i]}@gmail.com', password=f'{nombres[i]}{apellidos[i]}')
        user.save()
        lujo = Categoria(usuario=user, nombre='lujos')
        fijo = Categoria(usuario=user, nombre='fijos')
        deuda = Categoria(usuario=user, nombre='deudas')
        esencial = Categoria(usuario=user, nombre='esenciales')
        lujo.save()
        fijo.save()
        deuda.save()
        esencial.save()
        categories = [lujo, fijo, deuda]
        movimientos = ['zapatos', 'almuerzo', 'casa', 'arriendo', 'servicios', 'mascota', 'carro', 'comida', 'salida', 'paseo', 'spotify', 'netflix', 'HBO']
        direcciones = ['entrada', 'salida']
        for j in range(10):
            move = Movimiento(nombre=movimientos[random.randint(0, len(movimientos) - 1)], usuario=user, direccion=direcciones[random.randint(0, 1)], valor=random.randint(10000, 2000000), fecha=date.today(), categoria=categories[random.randint(0, 2)])
            move.save()


