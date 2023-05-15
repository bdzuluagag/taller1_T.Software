from wallet import connection


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
