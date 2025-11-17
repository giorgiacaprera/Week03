class Car:
# Variabile o attributo di classe, posseduta da ed uguale in tutti gli oggetti di Car
    wheels = 4

    """
    def __init__(self): 
        # Variabili o attributi di istanza: ogni oggetto creato a partire dalla classe Car
        # ne ha una propria copia e i suoi valori possono cambiare
        self.licensePlate = 0 
        self.bodyColor = ""
        self.turnedOn = False
    """

    def __init__(self, licensePlate, bodyColor):
        self.licensePlate = licensePlate
        self.bodyColor = bodyColor
        self.turnedOn = False

    def paint(self, color): # Riceve come parametro il nuovo colore
        self.bodyColor = color # Assegna color all'attributo self.bodyColor

    def turnOn(self): # Cambia lo stato dell'oggetto Car, mettendo turnedOn a True
        self.turnedOn = True

    def printYourself(self):
        print(self.licensePlate, self.bodyColor, self.turnedOn)

c1 = Car() # Python vede le () ed invoca __init__()

c2 = Car()

# Assegno all'attributo licensePlate di c1 un valore
c1.licensePlate = "AB123CD"

# Poi vi accedo e lo stampo nella console
print(c1.licensePlate)

# Stampo anche licensePlate di c2
print(c2.licensePlate)

# Stampo tutti gli attributi
print(c1.licensePlate, c1.bodyColor, c1.turnedOn)

# Oppure, invoco printYourself()
c1.paint("Green")
c1.turnOn()
c1.printYourself()

# La sintassi sopra è equivalente a
Car.printYourself(c1)

# Se in un qualunque punto del codice prendo il nome di un oggetto e scrivo

c1.hasBeenWashed = True # Sto definendo una variabile di istanza per quello specifico oggetto

# Con riferimento a wheels, in particolare, se scrivo

c1.wheels = 6 # Sto creando una nuova variabile/attributo DI ISTANZA (SOLO) per c1

# Con l'istruzione che segue, invece, cambio la variabileì/attributo DI CLASSE
Car.wheels = 8