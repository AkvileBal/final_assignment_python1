from collections import Counter
import datetime
from csv import reader, writer

class skaiciavimai:
    
    def gamintojai(eilutes):
        gamintojas=[]
        for i in eilutes:
            for j in i:
                j=i[1]
            gamintojas.append(j)
        return gamintojas

  
    def senienu_sarasas(eilutes):
        sarasas=[]
        dabar=datetime.datetime.today().year
        dabar0=int(dabar)
        for i in eilutes:
            for j in i:
                j=int(i[3])
                amzius=dabar0-j
            if amzius>10:
                sarasas.append(i)
        return sarasas 
      

class atsakymai:
    def automobilių_daugiau_nei_1(gamintojas):    
        
        p=Counter(gamintojas)
        p=dict(p)
        for raktas, reiksme in p.items():
            if reiksme>1:
                print(f'Šių gamintojų automobilių yra daugiau nei 1: {raktas}, jų yra: {reiksme}')
    

    def VW_sarasas(eilutes):
        print(f'Visų turimų VW automobilių sąrašas (valstybiai numeriai, gamintojas, modelis, gamybos metai):' )            
        for i in eilutes:
            for j in i:
                if j=='VW':
                    print(i)
    
    def failo_irasymas(sarasas):
        with open('senienos.csv', 'w', newline='') as failas:
            csv_writer=writer(failas)
            csv_writer.writerow(['Valstybiniai numeriai', 'Gamintojas', 'Modelis', 'Gamybos metai'])
            csv_writer.writerows(sarasas)
   

    def read_senienos(duomenys):
        with open('senienos.csv') as failas:
            duomenys=failas.readlines()
            print(duomenys)
 
 



    





