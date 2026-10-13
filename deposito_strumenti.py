import csv
class Strumento:
    def __init__(self,id_strumento , tipo, marca, anno, valore_euro):
        self.id_strumento= id_strumento
        self.tipo= tipo
        self.marca= marca
        self.anno= anno
        self.valore_euro= valore_euro
    def __str__(self):
        return (f"{self.id_strumento}-{self.tipo}-{self.marca}-{self.anno}-{self.valore_euro} euro")

class Prestito:
    def __init__(self, idprestito, data, id_strumento, cognome_allievo):
        self.idprestito= idprestito
        self.data= data
        self.id_strumento= id_strumento
        self.cognome_allievo= cognome_allievo

    def __str__(self):
        return self.idprestito + self.data + self.id_strumento +self.cognome_allievo

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile= responsabile
        self.contatore = 1
        self.strumenti = []
        self.prestiti= []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r") as csvfile:
            for riga in csvfile:
                valori=riga.strip().split(",")
                stru= Strumento(
                    id_strumento= valori[0],
                    tipo=valori[1],
                    marca = valori[2],
                    anno = int (valori[3]),
                    valore_euro = float(valori[4])
                )
                self.strumenti.append(stru)


        return self.strumenti

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        numero =0
        for s in self.strumenti:
            n=int(s.id_strumento[1:])
            if n>numero:
                numero=n
        id_strumento = "s" +str(numero+1)
        stru= Strumento(id_strumento, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(stru)
        return stru

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        ordinati=self.strumenti.copy()
        for i in range(len(ordinati)):
            for j in range(i+1 , len(ordinati)):
                if ordinati[i].marca > ordinati[j].marca:
                    temp = ordinati[i]
                    ordinati[i] = ordinati[j]
                    ordinati[j] = temp
        return ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        trovato=False

        for s in self.strumenti:
            if s.id_strumento==id_strumento:
                trovato=True
        if trovato== False:
            raise Exception("strumento non presente")

        for p in self.prestiti:
            if p.id_strumento==id_strumento:
                raise Exception("strumento in prestito")
        idprestito= "P" + str(self.contatore)
        p= Prestito (idprestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(p)
        self.contatore = self.contatore+1
        return p

    def termina_prestito(self, idprestito):
        """Termina un prestito in atto"""
        for p in self.prestiti:
            if p.idprestito == idprestito:
                self.prestiti.remove(p)
                return ("terminato correttamente")
        raise Exception("prestito non presente")
