class Pieza :
    def __init__(self, color: str, simbolo: str, nombre: str) -> None:
        self.color: str = color
        self.simbolo: str = simbolo
        self.nombre: str = nombre


    def describir(self) -> str:
        return self.nombre + " " + self.color
    
    def es_del_color(self, color: str) -> bool:
        return self.color == color
    
class Peon(Pieza) :
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo : str = "♙"
        else :
            simbolo : str = "♟"
        super().__init__(color , simbolo , "peon")

    def es_movimiento_valido(self , fila , fila1 , columna , columna1 , tablero) :
        es_movimiento_valido = False

        if self.color == "blanca" and fila1 == fila - 1 and columna == columna1 :
            if tablero[fila1][columna1] == "":
                es_movimiento_valido = True

        if self.color == "negras" and fila1 == fila + 1 and columna == columna1 :
            if tablero[fila1][columna1] == "" :
                es_movimiento_valido = True

        if self.color == "blanca" and fila == 7 and fila1 == fila - 2 and columna == columna1:
            if tablero[6][columna] != "" or tablero[5][columna] != "":
                es_movimiento_valido = False
            else:
                es_movimiento_valido = True

        if self.color == "negras" and fila == 2 and fila1 == fila + 2 and columna == columna1:
            if tablero[3][columna] != "" or tablero[4][columna] != "":
                es_movimiento_valido = False
            else:
                es_movimiento_valido = True

        if self.color == "blanca" and fila1 == fila - 1 and (columna1 == columna + 1 or columna1 == columna - 1):
            if tablero[fila1][columna1] != "" and tablero[fila1][columna1].color != self.color :
                es_movimiento_valido = True

        if self.color == "negras" and fila1 == fila + 1 and (columna1 == columna + 1 or columna1 == columna - 1):
            if tablero[fila1][columna1] != "" and tablero[fila1][columna1].color != self.color:
                es_movimiento_valido = True


        return es_movimiento_valido


class Torre(Pieza) :
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo : str = "♖"
        else :
            simbolo : str = "♜"
        super().__init__(color , simbolo , "torre")

    def es_movimiento_valido(self, fila , fila1 ,columna , columna1, tablero) :

        es_movimiento_valido = False

        if (fila == fila1 or columna == columna1) and (fila != fila1 or columna != columna1):
            es_movimiento_valido = True
            if columna == columna1 :

                if fila1 > fila:
                    for i in range(fila + 1, fila1):
                        if tablero[i][columna] != "":
                            es_movimiento_valido = False
                elif fila1 < fila :

                    for j in range(fila1 + 1, fila):
                        if tablero[j][columna] != "":
                            es_movimiento_valido = False
            elif fila == fila1 :
                if columna1 > columna:
                    for i in range(columna + 1, columna1):
                        if tablero[fila][i] != "":
                            es_movimiento_valido = False
                elif columna1 < columna :
                    for j in range(columna1 + 1 , columna) :
                        if tablero[fila][j] != "" :
                            es_movimiento_valido = False
                            
        return es_movimiento_valido
    

class Caballo(Pieza) :
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo : str = "♘"
        else :
            simbolo : str = "♞"
        super().__init__(color , simbolo , "caballo")

    def es_movimiento_valido(self , fila , fila1 , columna , columna1 , tablero) :
        es_movimiento_valido = False
        if (abs(fila1 - fila) == 2 and abs(columna1 - columna) == 1) or (abs(fila1 - fila) == 1 and abs(columna1 - columna) == 2):
            es_movimiento_valido = True

        return es_movimiento_valido

class Alfil(Pieza) :
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo : str = "♗"
        else :
            simbolo : str = "♝"
        super().__init__(color , simbolo , "alfil")

    def es_movimiento_valido(self , fila , fila1 , columna , columna1 , tablero):
        es_movimiento_valido = False
        if abs(fila1 - fila) == abs(columna1 - columna) and (fila != fila1 or columna != columna1):
            es_movimiento_valido = True

            if fila > fila1 and columna < columna1 :
                j = columna + 1
                for i in range ( fila - 1 , fila1 , -1) :
                    if tablero[i][j] != "" :
                        es_movimiento_valido = False
                    j += 1
            if fila > fila1 and columna > columna1 :
                j = columna - 1
                for i in range ( fila -1 , fila1 , -1) :
                    if tablero[i][j] != "":
                        es_movimiento_valido = False
                    j -= 1
            if fila < fila1 and columna < columna1 :
                j = columna + 1
                for i in range (fila + 1 , fila1):
                    if tablero[i][j] != "":
                        es_movimiento_valido = False
                    j += 1
            if fila < fila1 and columna > columna1 :
                j = columna - 1
                for i in range ( fila + 1 , fila1) :
                    if tablero[i][j] != "" :
                        es_movimiento_valido = False
                    j -= 1
        return es_movimiento_valido

class Rey(Pieza) :
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo : str = "♔"
        else :
            simbolo : str = "♚"
        super().__init__(color , simbolo , "rey")

    def es_movimiento_valido(self , fila , fila1 , columna , columna1 , tablero) :
        es_movimiento_valido = False
        if abs(fila1 - fila) <= 1 and abs(columna1 - columna) <= 1 and (fila != fila1 or columna != columna1):
            es_movimiento_valido = True

        return es_movimiento_valido

class Dama(Pieza) :
    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo : str = "♕"
        else :
            simbolo : str = "♛"
        super().__init__(color , simbolo , "dama")

    def es_movimiento_valido(self, fila, fila1, columna, columna1, tablero):
        torre = Torre(self.color)
        alfil = Alfil(self.color)
        
        if torre.es_movimiento_valido(fila, fila1, columna, columna1, tablero) or alfil.es_movimiento_valido(fila, fila1, columna, columna1, tablero):
            return True 
        else:
            return False

class Tablero :
    def __init__(self) -> None :
        self.tablero = []

    def tablero_construccion(self):
        for i in range (9) :
            fila_vacia : list = []
            for j in range (9):
                fila_vacia.append("")
            self.tablero.append(fila_vacia)
            
        self.tablero[0] = [".", "a ", "b ", "c ", "d ", "e ", "f ", "g ", "h "]

    def tablero_imprimir(self) :
        for i in range (9):
            for j in range (9):
                if i == 0 or j == 0 or self.tablero[i][j] == "":
                    print(self.tablero[i][j], end="    ")
                else:
                    print(self.tablero[i][j].simbolo, end="    ")
            print()
            print()

    def mover_pieza(self, fila, fila1, columna, columna1):
        pieza = self.tablero[fila][columna]
        self.tablero[fila1][columna1] = pieza
        self.tablero[fila][columna] = ""
            

tablero: Tablero = Tablero()

tablero.tablero_construccion()

tablero.tablero[8][5] = Rey("blanca")
tablero.tablero[8][4] = Dama("blanca")
tablero.tablero[8][3]= Alfil("blanca")
tablero.tablero[8][2]= Caballo("blanca")
tablero.tablero[8][1]= Torre("blanca")
tablero.tablero[8][6]= Alfil("blanca")
tablero.tablero[8][7]= Caballo("blanca")                   
tablero.tablero[8][8]= Torre("blanca")


for columna in range (1,9):
    tablero.tablero[7][columna]=Peon("blanca")

tablero.tablero[1][5] = Rey("negras")
tablero.tablero [1][4]= Dama("negras")               
tablero.tablero[1][3]= Alfil("negras")
tablero.tablero[1][2]= Caballo("negras")
tablero.tablero[1][1]= Torre("negras")
tablero.tablero[1][6]= Alfil("negras")
tablero.tablero[1][7]= Caballo("negras")                   
tablero.tablero[1][8]= Torre("negras")

for columna in range (1,9):
    tablero.tablero[2][columna]=Peon("negras")
                
for var in range (1,9):
    tablero.tablero[var][0]= 9 - var

import os

def actualizar_tablero():
    os.system("cls")
    tablero.tablero_imprimir()

tablero.tablero_imprimir()

columnas_dict = {".":0, "a ": 1, "b ": 2, "c ": 3, "d ": 4, "e ": 5, "f ": 6, "g ": 7, "h ": 8,}
filas_dict = {8: 1, 7: 2, 6: 3, 5: 4, 4: 5, 3: 6, 2: 7, 1: 8}

estado: str = "turno_blancas"

while estado != "salir":
    
    if estado == "turno_blancas":
        print("Turno de blancas")

        movimiento = input("Introduce origen y destino (o 'salir' para terminar):")
        
        if movimiento == "salir":
            estado: str = "salir"
            print("Fin de partida")
            break

        coordenadas = movimiento.split()

        if len(coordenadas) != 2:
            print("Debes introducir dos casillas")
            continue

        origen = coordenadas[0]
        destino = coordenadas[1]

        def es_casilla_valida(casilla):
            return len(casilla) == 2 and casilla[0] + " " in columnas_dict and int(casilla[1]) in filas_dict

        if not es_casilla_valida(origen) or not es_casilla_valida(destino) :
            print("Alguna de las casillas no es correcta")
            continue        

        def procesar_casilla(casilla) -> bool:
            if es_casilla_valida(casilla):
                print("Casillas válidas:", casilla)
                return True
            else :
                print("Casilla no válida")
                return False

        if not procesar_casilla(origen) or not procesar_casilla(destino):
            continue

        l = origen[0] + " "
        n = origen[1]
        num = int(n)

        l1 = destino[0] + " "
        n1 = destino[1]
        num1 = int(n1)

        def convertir_casilla():
            return num in filas_dict and l in columnas_dict and num1 in filas_dict and l1 in columnas_dict
        
        def pasar_fila_columna(casilla , casilla1):

            if convertir_casilla():
                fila = filas_dict[num]
                fila1 = filas_dict[num1]
                columna = columnas_dict[l]
                columna1 = columnas_dict[l1]
                pieza = tablero.tablero[fila][columna]
                pieza1 = tablero.tablero[fila1][columna1]
                if pieza == "":
                    pieza_print = "casilla vacía"
                else:
                    pieza_print = pieza.nombre

                if pieza1 == "":
                    pieza_print1 = "casilla vacía"
                else:
                    pieza_print1 = pieza1.nombre

                if pieza != "":
                    if estado == "turno_blancas":
                        if pieza.color == "blanca":
                            movimiento_valido = True
                        else:
                            print("No puedes mover una pieza de negras")
                            movimiento_valido = False
                    else:
                        if pieza.color == "negras":
                            movimiento_valido = True
                        else:
                            print("No puedes mover una pieza de blancas")
                            movimiento_valido = False
                else:
                    movimiento_valido = False
                    print("La casilla de origen está vacía")

                if movimiento_valido :
                    if pieza1 != "" :
                        if pieza.color == pieza1.color :
                            print("No se puede capturar")
                            destino_valido = False
                        else :
                            print("Se puede capturar")
                            destino_valido = True
                    else :
                        
                        destino_valido = True

                else :
                    destino_valido = False

                movimiento_valido = movimiento_valido and destino_valido

                if movimiento_valido :
                    if pieza.nombre == "torre" :
                        movimiento_valido = pieza.es_movimiento_valido(fila , fila1 , columna , columna1 , tablero.tablero)

                    elif pieza.nombre == "alfil":
                        movimiento_valido = pieza.es_movimiento_valido(fila, fila1, columna, columna1, tablero.tablero)

                    elif pieza.nombre == "caballo":
                        movimiento_valido = pieza.es_movimiento_valido(fila, fila1, columna, columna1, tablero.tablero)

                    elif pieza.nombre == "peon":
                        movimiento_valido = pieza.es_movimiento_valido(fila, fila1, columna, columna1, tablero.tablero)

                    elif pieza.nombre == "rey":
                        movimiento_valido = pieza.es_movimiento_valido(fila, fila1, columna, columna1, tablero.tablero)

                    elif pieza.nombre == "dama":
                        movimiento_valido = pieza.es_movimiento_valido(fila, fila1, columna, columna1, tablero.tablero)

                    if movimiento_valido:
                        tablero.mover_pieza(fila, fila1, columna, columna1)

                        if pieza.nombre == "peon":
                            if (pieza.color == "blanca" and fila1 == 1) or (pieza.color == "negras" and fila1 == 8):
                                tablero.tablero[fila1][columna1] = Dama(pieza.color)

                        actualizar_tablero()


                print("Hay un" , pieza_print ,"en la casilla", casilla , "y un",pieza_print1 , "en la casilla" , casilla1)

                return movimiento_valido

        movimiento_valido = pasar_fila_columna(origen, destino)

        if movimiento_valido:
            print("Puedes continuar con el movimiento")
        else:
            continue

        def cambio_turno_negras() :
            return "turno_negras"

        def cambio_turno_blancas():
            return"turno_blancas"

        estado = cambio_turno_negras()
        
    elif estado == "turno_negras" :
        print("Turno de negras")

        movimiento = input("Introduce origen y destino (o 'salir' para terminar):")
                
        if movimiento == "salir":
            estado: str = "salir"
            print("Fin de partida")
            break

        coordenadas = movimiento.split()

        if len(coordenadas) != 2:
            print("Debes introducir dos casillas")
            continue
        
        origen = coordenadas[0]
        destino = coordenadas[1]

        if not es_casilla_valida(origen) or not es_casilla_valida(destino) :
            print("Alguna de las casillas no es correcta")
            continue

        if not procesar_casilla(origen) or not procesar_casilla(destino):
            continue

        l = origen[0] + " "
        n = origen[1]
        num = int(n)
        l1 = destino[0] + " "
        n1 = destino[1]
        num1 = int(n1)

        movimiento_valido = pasar_fila_columna(origen , destino)

        if movimiento_valido:
            print("Puedes continuar con el movimiento")
        else:
            continue


        estado = cambio_turno_blancas()