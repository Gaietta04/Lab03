import csv
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
