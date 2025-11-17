from dipartimento import Dipartimento
from impiegato import Impiegato

i = Impiegato("Mario", "Rossi", 20000)

print(i) # Equivalente a print(i.__str__())

print(i.__repr__())

# Posso anche creare altri oggetti Impiegato ed aggiungerli ad una struttura dati
altroImpiegato = Impiegato("Gianna", "Verdi", 50000)

listaDiImpiegati = []

listaDiImpiegati.append(i)
listaDiImpiegati.append(altroImpiegato)

# Che posso poi scandire con un for e stampare
for impiegato in listaDiImpiegati:
    print(impiegato.__str__()) # Anche senza __str__()

# Posso anche introdurre il concetto di dipartimento:
# basta definire una nuova classe, Dipartimento (in dipartimento.py)

# Posso poi costruire un oggetto di quel tipo/quella classe
dipartimentoA = Dipartimento("Risorse umane") # Assegno il nome al dipartimento che creo

# Come faccio poi a rappresentare il fatto che un impiegato lavori in un
# determinato dipartimento?

# Aggiungo la variabile self._dipartimento alla class Impiegato

impiegato._dipartimento = dipartimentoA
