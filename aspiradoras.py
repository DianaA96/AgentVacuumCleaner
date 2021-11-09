import random
import time
from termcolor import colored
from IPython.display import clear_output, display_html


# Definimos una clase para dirigir el comportamiento de cada aspiradora
class VacuumCleaner:
    # Constructor, inicializa los valores de x y y en cero y pone un nombre a la aspiradora
    def __init__(self, name, m, n):
        self.name = name
        self.x = 1
        self.y = 1
        self.m = m
        self.n = n
        self.cost = 0;
        self.mapLearning = []
        aux = []
        for i in range(m):
            for j in range(n):
                aux.append([' '])
            self.mapLearning.append(aux)
            aux = []
        vacuumWorld[self.y][self.x].append(self.name)
        self.mapLearning[self.y][self.x] = ['-']
  
    def aspirar(self):
        if vacuumWorld[self.y][self.x][0] == '⚫':
            print(colored('ASPIRA', 'cyan'))
            vacuumWorld[self.y][self.x][0] = '   '
            global celdasAspiradas
            celdasAspiradas = celdasAspiradas + 1
    
    def limpiar(self):
        time.sleep(1)
        print("LIMPIA")
        imprimeHabitaciones()
        self.aspirar()
        self.mover()
        
    def mover(self):
        print("MUEVE")
        
        # Ocho direcciones posibles. Elige una al azar y se desplaza. Si no se puede mover ahí, se quedará en su lugar.
        # NO SE MUEVE SI EL ÍNDICE ESTÁ FUERA DE RANGO O SI HAY UNA ASPIRADORA EN ESE SITIO.
        # NO SE MUEVE SI YA HA VISITADO ESA HABITACIÓN CON ANTERIORIDAD.
        # ELECCIÓN DE MOVIMIENTO ALEATORIA
        
        eleccion = 1

        #ARRIBA
        if(eleccion == 1 and (self.y-1 >= 0)):
            if((vacuumWorld[self.y-1][self.x] == ['⚫'] or vacuumWorld[self.y-1][self.x] == ['   ']) and self.mapLearning[self.y-1][self.x] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y-1][self.x].append(self.name)
                self.mapLearning[self.y-1][self.x] = ['-']
                #print("ARRIBA")
                self.y = self.y-1
                self.cost = self.cost + 1
                #self.aspirar()
        
        eleccion = eleccion + 1
        
        #ABAJO
        if(eleccion == 2 and (self.y+1 < self.m)):
             if((vacuumWorld[self.y+1][self.x] == ['⚫'] or vacuumWorld[self.y+1][self.x] == ['   ']) and self.mapLearning[self.y+1][self.x] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y+1][self.x].append(self.name)
                self.mapLearning[self.y+1][self.x]= ['-']
                #print("ABAJO")
                self.y = self.y+1
                self.cost = self.cost + 1
                #self.aspirar()
        
        eleccion = eleccion + 1

        #DERECHA
        if(eleccion == 3 and (self.x+1 < self.n)):
            if((vacuumWorld[self.y][self.x+1] == ['⚫'] or vacuumWorld[self.y][self.x+1] == ['   ']) and self.mapLearning[self.y][self.x+1] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y][self.x+1].append(self.name)
                self.mapLearning[self.y][self.x+1] = ['-']
                #print("DERECHA")
                self.x = self.x+1
                self.cost = self.cost + 1
                #self.aspirar()
        
        
        eleccion = eleccion + 1
        
        #IZQUIERDA
        if(eleccion == 4 and (self.x-1 >= 0)):
            if((vacuumWorld[self.y][self.x-1] == ['⚫'] or vacuumWorld[self.y][self.x-1] == ['   ']) and self.mapLearning[self.y][self.x-1] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y][self.x-1].append(self.name)
                self.mapLearning[self.y][self.x-1] = ['-']
                #print("IZQUIERDA")
                self.x = self.x-1
                self.cost = self.cost + 1
                #self.aspirar()

        
        eleccion = eleccion + 1
        
        #SUPDER
        if(eleccion == 5 and self.x+1 < self.n and self.y-1 >= 0):
            if((vacuumWorld[self.y-1][self.x+1] == ['⚫'] or vacuumWorld[self.y-1][self.x+1] == ['   ']) and self.mapLearning[self.y-1][self.x+1] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y-1][self.x+1].append(self.name)
                self.mapLearning[self.y-1][self.x+1] = ['-']
                #print("SUPERIOR DERECHA")
                self.x = self.x+1
                self.y = self.y-1
                self.cost = self.cost + 1
                #self.aspirar()

        
        eleccion = eleccion + 1
        
        #SUPIZQ
        if(eleccion == 6 and (self.x-1 >= 0) and self.y-1 >= 0):
            if((vacuumWorld[self.y-1][self.x-1] == ['⚫'] or vacuumWorld[self.y-1][self.x-1] == ['   ']) and self.mapLearning[self.y-1][self.x-1] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y-1][self.x-1].append(self.name)
                self.mapLearning[self.y-1][self.x-1] = ['-']
                #print("SUPERIOR IZQUIERDA")
                self.x = self.x-1
                self.y = self.y-1
                self.cost = self.cost + 1
                #self.aspirar()

        eleccion = eleccion + 1
        
        #INFDER
        if(eleccion == 7 and (self.x+1 < self.n) and self.y+1 < self.m):
            if((vacuumWorld[self.y+1][self.x+1] == ['⚫'] or vacuumWorld[self.y+1][self.x+1] == ['   ']) and self.mapLearning[self.y+1][self.x+1] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y+1][self.x+1].append(self.name)
                self.mapLearning[self.y+1][self.x+1] = ['-']
                #print("INFERIOR DERECHA")
                self.x = self.x+1
                self.y = self.y+1
                self.cost = self.cost + 1
                #self.aspirar()

        
        eleccion = eleccion + 1
        
        #INFIZQ
        if(eleccion == 8 and (self.x-1 >= 0 and self.y+1 < self.m)):
            if((vacuumWorld[self.y+1][self.x-1] == ['⚫'] or vacuumWorld[self.y+1][self.x-1] == ['   ']) and self.mapLearning[self.y+1][self.x-1] == [' ']):
                vacuumWorld[self.y][self.x].pop(vacuumWorld[self.y][self.x].index(self.name))
                vacuumWorld[self.y+1][self.x-1].append(self.name)
                self.mapLearning[self.y+1][self.x-1] = ['-']
                #print("INFERIOR IZQUIERDA")
                self.x = self.x-1
                self.y = self.y+1
                self.cost = self.cost + 1
                #self.aspirar()

# Definimos las habitaciones que indica el usuario (n x m)
m = int(input("Ingrese m: "))
n = int(input("Ingrese n: "))
inputPorcentajeSuciedad = int(input("Ingrese el porcentaje de suciedad inicial de las habitaciones: "))
tiempo = int(input("Ingrese el tiempo máximo de ejecución [en segundos]: "))
celdasSucias = int(inputPorcentajeSuciedad/100 * (m * n))
numAspiradoras = int(input("Ingrese el numero de aspiradoras: "))
contCeldasSucias = 0
vacuumWorld = []
aux = []
lista = []
celdasAspiradas = 0

for a in range(celdasSucias):
    lista.append(['⚫'])
for b in range((m*n) - celdasSucias):
    lista.append(['   '])\
                    
random.shuffle(lista)
cont = 0

for i in range(m):
    for j in range(n):
        aux.append(lista[cont])
        cont = cont + 1
    vacuumWorld.append(aux)
    aux = []

def imprimeHabitaciones():
    print("Habitación: ")
    for i in range(m):
        print(vacuumWorld[i])
    print("")

print("Mundo inicial: ")
imprimeHabitaciones()

aspiradoras = []
mostrarContador = []

for h in range(numAspiradoras):
    name = "A" + str(h+1)
    aspiradoras.append(VacuumCleaner(name, m, n))
    mostrarContador.append(0)

inicio = time.time()
current = time.time()

while current - inicio <= tiempo or celdasAspiradas == celdasSucias:
    current = time.time()
    for w in range(numAspiradoras):
        aspiradoras[w].limpiar()
        mostrarContador[w] = int(aspiradoras[w].cost)
        print("Desempeño: ", mostrarContador)

print("Tiempo de ejecución:", (current-inicio))