# Nella OOP una regola d'oro è quella di "proteggere" gli attibuti
# definendoli privati, in Python con _ (lasca) o __ (seria)

class Libro:
    def __init__(self):
        self.__titolo = "" # __ Protezione forte (error)
        self.__autore= ""
        self.__numPagine= 0
        self._anno = 0 # Protezione più lasca (warning)

    # Restituisce l'anno
    """
    def dammiAnno(self):
        return self.__anno
    """

    # Imposta l'anno in maniera controllata
    """
    def impostaAnno(self, anno):
        if anno<0:
            print("Tentativo di impostare anno negativo")
        else:
            self.__anno = anno
    """

    @property
    def anno(self): # Metodo getter per l'attributo anno
        return self._anno

    @anno.setter
    def anno(self, anno):
        if anno<0:
            print("Tentativo di impostare anno negativo")
        else:
            self._anno = anno

l1 = Libro()

# L'attributo non è più accessibile (o quasi, è più difficile accedere in
# lettura/scrittura al valore
print(l1.__titolo)

l1._anno = 2008
l1._anno = -500

# Come accedere ad un attributo non visibile?
l1.impostaAnno(-500)

# Se ho dichiarato getter e setter con i decoratori
l1.anno = 2008 # Pyhton chiama il setter
print(l1.anno) # Python chiama il getter

l1.__repr__()