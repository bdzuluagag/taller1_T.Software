def readIncomes(movements):
    if not movements:
        return
    movements = movements.split('.')
    with open('wallet/movements.txt', 'a') as file:
        for movement in movements:
            file.write('in, ' + movement + ', \n')


def readExits(movements):
    if not movements:
        return
    movements = movements.split('.')
    with open('wallet/movements.txt', 'a') as file:
        for movement in movements:
            file.write('out, ' + movement + ', \n')


def read_movements(incomes, exits):
    readExits(exits)
    readIncomes(incomes)
    with open('wallet/movements.txt', 'r') as file:
        ans = []
        for line in file.readlines():
            lin = line.split(',')
            direction = 'entrada -> ' if lin[0] == 'in' else 'salida -> '
            ans += [direction + 'nombre: ' + lin[1] + ' valor: ' + lin[2] + ' categoria: ' + lin[3]]
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