import csv
from dataclasses import dataclass
@dataclass
class Strumento:
    id_strumento:str
    tipo: str
    marca : str
    anno : int
    valore_euro : float
@dataclass
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile= responsabile
        self.strumenti = []

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
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
