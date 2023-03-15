from wallet import connection


def readIncomes(movements):
    if not movements:
        return
    movements = movements.split('.')
    connection.create_movement(movements, 'entrada')


def readExits(movements):
    if not movements:
        return
    movements = movements.split('.')
    connection.create_movement(movements, 'salida')


def read_movements(incomes, exits):
    readExits(exits)
    readIncomes(incomes)
    movements = connection.search_user_movements()
    ans = []
    for movement in movements:
        ans.append(f'nombre: {movement[0]}, {movement[3]}, valor: {movement[4]}, fecha: {movement[5].strftime("%m/%d/%Y")}, categoría: {movement[6]}')
    return ans


def consult_category(category):
    if not category:
        return
    movements = connection.search_movement_category(category)
    ans = []
    for movement in movements:
        ans.append(
            f'nombre: {movement[0]}, {movement[3]}, valor: {movement[4]}, fecha: {movement[5].strftime("%m/%d/%Y")}, categoría: {movement[6]}')
    return ans


