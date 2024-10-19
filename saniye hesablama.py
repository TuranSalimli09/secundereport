from datetime import datetime
import time
import os

def hesapla_yas(birthdate):
    indiki_tarix = datetime.now()
    dogum_tarixi = datetime.strptime(birthdate, "%d/%m/%Y")
    keçen_vaxt = (indiki_tarix - dogum_tarixi).total_seconds()
    return keçen_vaxt
dogum_tarixi = input("Doğum tarihinizi (GG/AA/YYYY formatında) girin: ")
birth_hour = int(input("hour:"))
birth_minute = int(input("minute:"))
birth_second = int(input("second:"))
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    yas_saniye = hesapla_yas(dogum_tarixi)
    print(f"İndiye qeder yaşadığınız saniye sayısı: {yas_saniye} saniye")
    time.sleep(1)