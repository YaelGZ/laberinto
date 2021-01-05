import queue


def laberinto1():
    laberinto = []
    laberinto.append(["#","#", "#", "#", "#", "O","#"])
    laberinto.append(["#"," ", " ", " ", "#", " ","#"])
    laberinto.append(["#"," ", "#", " ", "#", " ","#"])
    laberinto.append(["#"," ", "#", " ", " ", " ","#"])
    laberinto.append(["#"," ", "#", "#", "#", " ","#"])
    laberinto.append(["#"," ", " ", " ", "#", " ","#"])
    laberinto.append(["#","#", "#", "#", "#", "X","#"])

    return laberinto

def laberinto2():
    laberinto = []
    laberinto.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    laberinto.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    laberinto.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    laberinto.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    laberinto.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    laberinto.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    laberinto.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    laberinto.append(["#"," ", " ", " ", "#", " ", " ", " ", "#"])
    laberinto.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return laberinto


def imprimirLaberinto(laberinto, path=""):
    for x, pos in enumerate(laberinto[0]):
        if pos == "O":
            inicio = x

    i = inicio
    j = 0
    pos = set()
    for move in path:
        if move == "Izq":
            i -= 1

        elif move == "Der":
            i += 1

        elif move == "Arriba":
            j -= 1

        elif move == "Abajo":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(laberinto):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def validar(laberinto, moves):
    for x, pos in enumerate(laberinto[0]):
        if pos == "O":
            inicio = x

    i = inicio
    j = 0
    for move in moves:
        if move == "Izq":
            i -= 1

        elif move == "Der":
            i += 1

        elif move == "Arriba":
            j -= 1

        elif move == "Abajo":
            j += 1

        if not(0 <= i < len(laberinto[0]) and 0 <= j < len(laberinto)):
            return False
        elif (laberinto[j][i] == "#"):
            return False

    return True


def salida(laberinto, moves):
    for x, pos in enumerate(laberinto[0]):
        if pos == "O":
            inicio = x

    i = inicio
    j = 0
    for move in moves:
        if move == "Izq":
            i -= 1

        elif move == "Der":
            i += 1

        elif move == "Arriba":
            j -= 1

        elif move == "Abajo":
            j += 1

    if laberinto[j][i] == "X":
        print("Movimientos: " + moves)
        imprimirLaberinto(laberinto, moves)
        return True

    return False


# MAIN

nums = queue.Queue()
nums.put("")
add = ""
laberinto  = laberinto2()

while not salida(laberinto, add): 
    add = nums.get()
    #imprmir(add)
    for j in ["Izq", "Der", "Arriba", "Abajo"]:
        put = add + j
        if validar(laberinto, put):
            nums.put(put)
