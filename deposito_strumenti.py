import csv
import dataclasses

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore
    def __str__(self):
        return f"{self.codice} - {self.tipo} - {self.marca} - {self.anno_acquisto} - {self.valore} euro"
class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo
    def __str__(self):
        return f"{self.codice} - {self.data} - {self.id_strumento} - {self.cognome_allievo}"

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome             #memorizza il nome del deposito
        self.responsabile = responsabile        #memorizza il nome del responsabile
        self.strumenti = []          #creazione lista vuota in cui inserirò gli stumenti musicali
        self.prestiti =[]            #crea una lista vuota in cui ci sono i prestiti in corso
        self.numero_prestiti = 0     #crea un contatore che parte da zero. Assegnerà  un codice progresivo ad ogni prestito

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r") as file:
            lettore = csv.reader(file)
            for riga in lettore:
                if len(riga) == 5:
                    strumento = Strumento(riga[0], riga[1], riga[2], int(riga[3]), float(riga[4]))
                    self.strumenti.append(strumento)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        numero = 0
        for strumento in self.strumenti:
            codice_numero = int(strumento.codice[1:])
            if codice_numero > numero:
                numero = codice_numero
        nuovo_codice = "S" + str(numero + 1)
        nuovo = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo)
        return nuovo

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti, key = lambda strumento: strumento.marca)

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        trovato = False
        for strumento in self.strumenti:
            if strumento.codice == id_strumento:
                trovato = True
        if not trovato:
            raise Exception("Strumento non presente nel deposito")
        for prestito in self.prestiti:
            if prestito.id_strumento == id_strumento:
                raise Exception("Strumento già in prestito")
        self.numero.prestiti += 1
        codice = "P" + str(self.numero_prestiti)
        nuovo = Prestito(
            codice, data, id_strumento, cognome_allievo
        )
        self.prestiti.append(nuovo)
        return nuovo

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for prestito in self.prestiti:
            if prestito.codice == id_prestito:
                self.prestiti.remove(prestito)
                return
        raise Exception("Prestito non trovato")