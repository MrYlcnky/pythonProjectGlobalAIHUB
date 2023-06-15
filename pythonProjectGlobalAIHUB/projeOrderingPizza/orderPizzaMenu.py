import csv
import pandas as pd
import numpy as np
import datetime
sepetList = []# bu bizim sepete eklediğimiz ürünlerin fiyatını ekliyeceğimiz listemiz
def main():
    txtRead() # burda Menu.txt dosyasını okuyoruz.
    bayrak = True
    while bayrak:
        number = int(input("Lütfen pizza açıklmasını okumak için pizza numarasını giriniz: ")) # seçeceğimiz pizzanın numarasını bu number değişkeninde tutuyotuz.
        pizzaSec(number) # pizzayı seçtikten sonra sos eklemek isteyip istemediğimizi bu fonksiyonun içinde soruyoruz.
        baska = input("Siparişin sonlansın mı? (E/H): ") # siparişe devam mı tamam mı burda öğreniyoruz. eger 'e' karakreriini
        # tuşlarsak sepete ürün ekleyemiyeceğiz. 'e' karakterinden farklı herhangi bir tuşa basarsak sepete eklemeye devam etmiş olcaz
        if baska == 'e':
            bayrak = False
    fatura() #ödenecek tutar karşımıza gelir.
    veriEkle() # kullanıcı verilerini veritabanına burda ekliyoruz.
def veriEkle():
    tarih = datetime.datetime.now()
    isim = input("adınız: ")
    kart_no = input("kart numarası: ")
    kart_sifre = input("kart sifre: ")

    with open('Orders_Database.csv', mode='w', newline='', encoding='utf-8-sig') as file:
        fieldnames = ['Name', 'kart no', 'kart sifre', 'sipariş tarihi']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Name': isim, 'kart no': kart_no, 'kart sifre': kart_sifre,'sipariş tarihi':tarih})

def txtRead():
    with open("Menu.txt","r") as menu:
        icerik = menu.read()
        print(icerik)
def pizzaSec(number):
    bayrak = True
    if number == 1:
        klasikpizza = Klasik()
        fiyat = 0
        while bayrak:
            sos = sosEkle()
            fiyat = fiyat + sos
            if(sos == 0):
                bayrak = False
        print(f"fiyat: {str(klasikpizza.cost + fiyat)}")
        topla = klasikpizza.cost + fiyat
        sepet(topla)
        return klasikpizza
    elif number == 2:
        margarita = Margarita()
        fiyat = 0
        while bayrak:
            sos = sosEkle()
            fiyat = fiyat + sos
            if (sos == 0):
                bayrak = False
        print(f"fiyat: {str(margarita.cost + fiyat)}")
        topla = margarita.cost + fiyat
        sepet(topla)
        return margarita
    elif number == 3:
        turkpizza = TurkPizza()
        fiyat = 0
        while bayrak:
            sos = sosEkle()
            fiyat = fiyat + sos
            if (sos == 0):
                bayrak = False
        print(f"fiyat: {str(turkpizza.cost + fiyat)}")
        topla = turkpizza.cost + fiyat
        sepet(topla)
        return turkpizza
    elif number == 4:
        sade = SadePizza()
        fiyat = 0
        while bayrak:
            sos = sosEkle()
            fiyat = fiyat + sos
            if (sos == 0):
                bayrak = False
        print(f"fiyat: {str(sade.cost + fiyat)}")
        topla = sade.cost + fiyat
        sepet(topla)
        return sade
    else:
        return "Lütfen geçerli bir numara giriniz."
def sosEkle():
    a = input("sos eklicek misin(e/h): ")
    if a == 'e':
        number = int(input("sos numarası gir: "))
        if number == 11:
            return Zeytin.cost
        elif number == 12:
            return Mantar.cost
        elif number == 13:
            return KeciPeyneri
        elif number == 14:
            return Et.cost
        elif number == 15:
            return Sogan.cost
        elif number == 16:
            return Misir.cost
        else:
            return "Lütfen geçerli bir numara giriniz."
    else:
        return 0
def sepet(fiyat):
    sepetList.append(fiyat)
def fatura():
    toplam = 0
    for i in sepetList:
        toplam = toplam + i
    print(f"ödenecek tutar: {toplam}")

class Pizza:
    cost = 28
    def __init__(self):
        self.cost = self.get_cost()
        description = self.get_description()
        print(description + str(self.cost) + "TL")
    def get_description(self):
        return f"Sade pizzamızın içinde {Kasar.des} ve {PizzaSosu.des} vardır. fiyat: "

    def get_cost(self):
        toplam = Kasar.cost + PizzaSosu.cost
        return toplam
class TurkPizza(Pizza):
    cost = 0
    self = ''
    def __init__(self):
        self.cost = self.get_cost() + Pizza.cost
        self.description = self.get_description()
        print(self.description + str(self.cost) + "TL")
    def get_description(self):
        return f"Türk Pizzamınızın içinde {Et.des}, {Zeytin.des}, {KeciPeyneri.des} and {Sogan.des} vardır. Fiyat: "
    def get_cost(self):
        toplam = Zeytin.cost + Et.cost + KeciPeyneri.cost + Sogan.cost
        return toplam
class Klasik(Pizza):
    cost = 0
    self = ''
    def __init__(self):
        self.cost = self.get_cost() + Pizza.cost
        self.description = self.get_description()
        print(self.description + str(self.cost) + "TL")

    def get_description(self):
        return f"Klasik Pizzamınızın içinde {Sucuk.des}, {Zeytin.des}, {Misir.des} and {Mantar.des} vardır. Fiyat: "

    def get_cost(self):
        toplam = Zeytin.cost + Sucuk.cost + Misir.cost + Mantar.cost
        return toplam
class Margarita(Pizza):
    cost = 0
    self = ''
    def __init__(self):
        self.cost = self.get_cost() + Pizza.cost
        self.description = self.get_description()
        print(self.description + str(self.cost) + "TL")
    def get_description(self):
        return f"Margarita Pizzamınızın içinde {Domates.des} and {Feslegen.des} vardır. Fiyat: "

    def get_cost(self):
        toplam = Domates.cost + Feslegen.cost
        return toplam
class SadePizza(Pizza):
    pass
class Decorator(Pizza):
    cost = 0
class Zeytin(Decorator):
    cost = 5
    des = "zeytin"
class Mantar(Decorator):
    cost = 6
    des = "mantar"
class KeciPeyneri(Decorator):
    cost = 7
    des = "keçi peyniri"
class Et(Decorator):
    cost = 30
    des = "et"

class Sogan(Decorator):
    cost = 8
    des = "sogan"
class Misir(Decorator):
    cost = 9
    des = "misir"
class Sucuk(Decorator):
    cost = 25
    des = "sucuk"
class Feslegen(Decorator):
    cost = 3
    des = "feslegen"
class Domates(Decorator):
    cost = 4
    des = "domates"
class Kasar(Decorator):
    cost = 25
    des = "kasar"
class PizzaSosu(Decorator):
    cost = 3
    des = "pizza sosu"
if __name__ == "__main__":
    main()