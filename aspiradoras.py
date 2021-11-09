import random
import time
from termcolor import colored

# Definimos una clase para dirigir el comportamiento de cada aspiradora
class VacuumCleaner:
    # Constructor, inicializa los valores de x y y en cero y pone un nombre a la aspiradora
    def __init__(self, name, m, n):
        self.name = name
        self.x = 1
        self.y = 1
        self.m = m
        self.n = n
        #self.mapLearning = []
        vacuumWorld[self.y][self.x].append(self.name)
  
    def aspirar(self):
        if vacuumWorld[self.y][self.x][0] == '⚫':
            print(colored('ASPIRA', 'cyan'))
            vacuumWorld[self.y][self.x][0] = '   '
    
    def limpiar(self):
        #time.sleep(1)
        print("LIMPIA")
        imprimeHabitaciones()
        self.aspirar()
        self.mover()
        
        
    def mover(self):
        print("MUEVE")
        
        # Ocho direcciones posibles. Elige una al azar y se desplaza. Si no se puede mover ahí, se quedará en su lugar.
        #NO SE MUEVE SI EL ÍNDICE ESTÁ FUERA DE RANGO O SI HAY UNA ASPIRADORA EN ESE SITIO.
        #ELECCION DE MOVIMIENTO ALEATORIA
        
        eleccion = random.choice([1, 2, 3, 4, 5, 6, 7, 8])

        #ARRIBA
        if(eleccion == 1 and (self.y-1 >= 0)):
            if(vacuumWorld[self.y-1][self.x] == ['⚫'] or vacuumWorld[self.y-1][self.x] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y-1][self.x].append(self.name)
                #print("ARRIBA")
                self.y = self.y-1
                self.limpiar()

        #ABAJO
        elif(eleccion == 2 and (self.y+1 < self.m)):
             if(vacuumWorld[self.y+1][self.x] == ['⚫'] or vacuumWorld[self.y+1][self.x] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y+1][self.x].append(self.name)
                #print("ABAJO")
                self.y = self.y+1
                self.limpiar()

        #DERECHA
        elif(eleccion == 3 and (self.x+1 < self.n)):
            if(vacuumWorld[self.y][self.x+1] == ['⚫'] or vacuumWorld[self.y][self.x+1] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y][self.x+1].append(self.name)
                #print("DERECHA")
                self.x = self.x+1
                self.limpiar()

        #IZQUIERDA
        elif(eleccion == 4 and (self.x-1 >= 0)):
            if(vacuumWorld[self.y][self.x-1] == ['⚫'] or vacuumWorld[self.y][self.x-1] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y][self.x-1].append(self.name)
                #print("IZQUIERDA")
                self.x = self.x-1
                self.limpiar()

        #SUPDER
        elif(eleccion == 5 and self.x+1 < self.n and self.y-1 >= 0):
            if(vacuumWorld[self.y-1][self.x+1] == ['⚫'] or vacuumWorld[self.y-1][self.x+1] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y-1][self.x+1].append(self.name)
                #print("SUPERIOR DERECHA")
                self.x = self.x+1
                self.y = self.y-1
                self.limpiar()

        #SUPIZQ
        elif(eleccion == 6 and (self.x-1 >= 0) and self.y-1 >= 0):
            if(vacuumWorld[self.y-1][self.x-1] == ['⚫'] or vacuumWorld[self.y-1][self.x-1] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y-1][self.x-1].append(self.name)
                #print("SUPERIOR IZQUIERDA")
                self.x = self.x-1
                self.y = self.y-1
                self.limpiar()

        #INFDER
        elif(eleccion == 7 and (self.x+1 < self.n) and self.y+1 < self.m):
            if(vacuumWorld[self.y+1][self.x+1] == ['⚫'] or vacuumWorld[self.y+1][self.x+1] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y+1][self.x+1].append(self.name)
                #print("INFERIOR DERECHA")
                self.x = self.x+1
                self.y = self.y+1
                self.limpiar()

        #INFIZQ
        elif(eleccion == 8 and (self.x-1 >= 0 and self.y+1 < self.m)):
            if(vacuumWorld[self.y+1][self.x-1] == ['⚫'] or vacuumWorld[self.y+1][self.x-1] == ['   ']):
                vacuumWorld[self.y][self.x].pop(1)
                vacuumWorld[self.y+1][self.x-1].append(self.name)
                #print("INFERIOR IZQUIERDA")
                self.x = self.x-1
                self.y = self.y+1
                self.limpiar()

# Definimos las habitaciones que indica el usuario (n x m)
m = int(input("Ingrese m: "))
n = int(input("Ingrese n: "))
vacuumWorld = []
aux = []

for i in range(m):
    for j in range(n):
        aux.append([random.choice(['⚫', '   '])])
    vacuumWorld.append(aux)
    aux = []

def imprimeHabitaciones():
    print("Habitación: ")
    for i in range(m):
        print(vacuumWorld[i])
    print("")

print("Mundo inicial: ")
imprimeHabitaciones()

A1 = VacuumCleaner("A1", m, n)
A2 = VacuumCleaner("A2", m, n)
A3 = VacuumCleaner("A3", m, n)
A4 = VacuumCleaner("A4", m, n)
A5 = VacuumCleaner("A5", m, n)
A6 = VacuumCleaner("A6", m, n)
A7 = VacuumCleaner("A7", m, n)
A8 = VacuumCleaner("A8", m, n)
A9 = VacuumCleaner("A9", m, n)
A10 = VacuumCleaner("A10", m, n)
A11 = VacuumCleaner("A11", m, n)
A12 = VacuumCleaner("A12", m, n)

for z in range(100):
    A1.limpiar()
    A2.limpiar()
    A3.limpiar()
    A4.limpiar()
    A5.limpiar()
    A6.limpiar()
    A7.limpiar()
    A8.limpiar()
    A9.limpiar()
    A10.limpiar()
    A11.limpiar()
    A12.limpiar()