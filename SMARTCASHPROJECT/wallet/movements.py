def readIncomes(movements):
    if not movements:
        return []
    movements = movements.split('.')
    ans = []
    for movement in movements:
        mov = movement.split(',')
        ans += ['entrada -> ' + ' nombre: ' + mov[0] + ' valor: ' + mov[1] + ' categoría: ' + mov[2]]
    return ans


def readExits(movements):
    if not movements:
        return []
    movements = movements.split('.')
    ans = []
    for movement in movements:
        mov = movement.split(',')
        ans += ['salida -> ' + ' nombre: ' + mov[0] + ' valor: ' + mov[1] + ' categoría: ' + mov[2]]
    return ans