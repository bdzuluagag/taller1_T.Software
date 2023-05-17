from wallet import connection
import csv
from datetime import datetime


def readIncomes(movements, user):
    if not movements:
        return
    movements = movements.split('.')
    connection.create_movement(movements, 'entrada', user)


def readExits(movements, user):
    if not movements:
        return
    movements = movements.split('.')
    connection.create_movement(movements, 'salida', user)


def read_movements(incomes, exits, user):
    readExits(exits, user)
    readIncomes(incomes, user)
    movements = connection.search_user_movements(user)
    return movements


def consult_category(category, user):
    if not category:
        return
    movements = connection.search_movement_category(category, user)
    return movements


def consult_user_lux(user):
    movements = connection.search_user_movements(user)
    dic = {}
    for movement in movements:
        if movement.categoria in dic:
            dic[movement.categoria] += movement.valor
        else:
            dic[movement.categoria] = movement.valor
    return dic


def generate_movements_csv(movements, user):
    with open(f'static/user_movements/{user.username}_movements.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        header = ['nombre', 'direccion', 'valor', 'fecha', 'categoria']
        writer.writerow(header)
        for movement in movements:
            line = [movement.nombre, movement.direccion, movement.valor, movement.fecha.__str__(), movement.categoria.nombre]
            writer.writerow(line)


def date_estimated(goals):
    dates = []
    for goal in goals:
        passed_days = (datetime.today().date() - goal.fecha_creacion).days
        if goal.cantidad_actual != 0:
            estimated = (goal.cantidad_meta * passed_days / goal.cantidad_actual) - passed_days
            goal.dias_estimados = int(round(estimated))
            goal.save()
