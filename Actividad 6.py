class Jugador:
    def __init__(self, apellido, dorsal, posicion, goles, minutos_jugados):
        self.apellido = apellido
        self.dorsal = dorsal
        self.posicion = posicion
        self.goles = goles
        self.minutos_jugados = minutos_jugados

    def mostrar_informacion(self):
        print(f"Apellido: {self.apellido}, Dorsal: {self.dorsal}, Posición: {self.posicion}, Minutos Jugados: {self.minutos_jugados}")
        
class Delantero(Jugador):
    def __init__(self, apellido, dorsal, posicion, goles, minutos_jugados):
        super().__init__(apellido, dorsal, posicion, goles, minutos_jugados)
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Goles: {self.goles}")

class Mediocampista(Jugador):
    def __init__(self, apellido, dorsal, posicion, goles, minutos_jugados):
        super().__init__(apellido, dorsal, posicion, goles, minutos_jugados)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Goles: {self.goles}")

class Defensor(Jugador):
    def __init__(self, apellido, dorsal, posicion, goles, minutos_jugados):
        super().__init__(apellido, dorsal, posicion, goles, minutos_jugados)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Goles: {self.goles}")
                 
class Arquero(Jugador):
    def __init__(self, apellido, dorsal, posicion, minutos_jugados):
        super().__init__(apellido, dorsal, posicion, 0, minutos_jugados)
    def mostrar_informacion(self):
        super().mostrar_informacion() 
        

lista_jugadores = []

def ingresar_jugador():
    global dc, mc, df, arq, lista_jugadores
    salir = False
    while salir == False:
        print("En que posición juega el jugador?")
        print("1. Delantero")
        print("2. Mediocampista")
        print("3. Defensor")
        print("4. Arquero")
        print("Presione cualquier numero para volver")
        posicion = int(input("Seleccione una opción: "))
        if posicion == 1:
            apellido = input("Ingrese el apellido del jugador: ")
            dorsal = int(input("Ingrese el dorsal del jugador: "))
            goles = int(input("Ingrese la cantidad de goles: "))
            minutos_jugados = int(input("Ingrese los minutos jugados: "))
            nuevo_jugador = Delantero(apellido, dorsal, "Delantero", goles, minutos_jugados)
            if not lista_jugadores:
                lista_jugadores = []
                lista_jugadores.append(nuevo_jugador)
            else:
                lista_jugadores.append(nuevo_jugador)
            return print("Jugador ingresado correctamente.")
        elif posicion == 2:
            apellido = input("Ingrese el apellido del jugador: ")
            dorsal = int(input("Ingrese el dorsal del jugador: "))
            goles = int(input("Ingrese la cantidad de goles: "))
            minutos_jugados = int(input("Ingrese los minutos jugados: "))
            nuevo_jugador = Mediocampista(apellido, dorsal, "Mediocampista", goles, minutos_jugados)
            if not lista_jugadores:
                lista_jugadores = []
                lista_jugadores.append(nuevo_jugador)
            else:
                lista_jugadores.append(nuevo_jugador)
            return print("Jugador ingresado correctamente.")
        elif posicion == 3:
            apellido = input("Ingrese el apellido del jugador: ")
            dorsal = int(input("Ingrese el dorsal del jugador: "))
            goles = int(input("Ingrese la cantidad de goles: "))
            minutos_jugados = int(input("Ingrese los minutos jugados: "))
            nuevo_jugador = Defensor(apellido, dorsal, "Defensor", goles, minutos_jugados)
            if not lista_jugadores:
                lista_jugadores = []
                lista_jugadores.append(nuevo_jugador)
            else:
                lista_jugadores.append(nuevo_jugador)
            return print("Jugador ingresado correctamente.")
        elif posicion == 4:
            apellido = input("Ingrese el apellido del jugador: ")
            dorsal = int(input("Ingrese el dorsal del jugador: "))
            minutos_jugados = int(input("Ingrese los minutos jugados: "))
            nuevo_jugador = Arquero(apellido, dorsal, "Arquero", minutos_jugados)
            if not lista_jugadores:
                lista_jugadores = []
                lista_jugadores.append(nuevo_jugador)
            else:
                lista_jugadores.append(nuevo_jugador)  
        else:
            print("Volviendo al menú principal...")
            salir = True

def mostrar_jugadores():
    global lista_jugadores
    if not lista_jugadores:
        print("No hay jugadores ingresados.")
    else:
        print("Plantilla temporada 2024/2025")
        print("-----------------------------")
        print("Arqueros:")
        for jugador in lista_jugadores:
            if isinstance(jugador, Arquero):
                jugador.mostrar_informacion()
        print("-----------------------------")    
        print("Defensores:")      
        for jugador in lista_jugadores:
            if isinstance(jugador, Defensor):
                jugador.mostrar_informacion()
        print("-----------------------------")
        print("Mediocampistas:")
        for jugador in lista_jugadores:
            if isinstance(jugador, Mediocampista):
                jugador.mostrar_informacion()
        print("-----------------------------")
        print("Delanteros:")
        for jugador in lista_jugadores:
            if isinstance(jugador, Delantero):
                jugador.mostrar_informacion()
        print("-----------------------------")
            


def Menu():
    salirMenu = False
    while salirMenu == False:
        print("1. Ingresar Jugador")
        print("2. Mostrar Jugadores")
        print("3. Salir")
        eleccion= int(input("Seleccione una opción: "))
        if eleccion == 1:
            ingresar_jugador()
        elif eleccion == 2:
            mostrar_jugadores()
        else:
            print("Saliendo del programa.")
            salirMenu = True

def main():
    if __name__ == "__main__":
        Menu()

main()