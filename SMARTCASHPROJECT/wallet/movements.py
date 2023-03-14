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
    with open('wallet/movements.txt', 'r') as file:

        ans = []
        for line in file.readlines():
            print(line.split(',')[3], category)
            if line.split(',')[3] == ' ' + category:
                lin = line.split(',')
                direction = 'entrada -> ' if lin[0] == 'in' else 'salida -> '
                ans += [direction + 'nombre: ' + lin[1] + ' valor: ' + lin[2] + ' categoria: ' + lin[3]]
        print(ans)

    return ans

