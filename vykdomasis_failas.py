import uzduotis_kopija


with open('Automobiliai.txt') as failas:
    eilutes=[]
    for eilute in failas:
        eilute=eilute.rstrip('\n')
        isskaidyta=eilute.split(',')
        eilutes.append(isskaidyta)

if len(eilutes)<=0:
    raise("Įmonė neturi automobilių")
    

skaiciavimas=uzduotis_kopija.skaiciavimai.gamintojai(eilutes)

atsakymas=uzduotis_kopija.atsakymai.automobilių_daugiau_nei_1(skaiciavimas)

VW_sarasas1=uzduotis_kopija.atsakymai.VW_sarasas(eilutes)

senienu_skaiciavmas=uzduotis_kopija.skaiciavimai.senienu_sarasas(eilutes)

csv_failas=uzduotis_kopija.atsakymai.failo_irasymas(senienu_skaiciavmas)

read_csv_failas=uzduotis_kopija.atsakymai.read_senienos(csv_failas)
