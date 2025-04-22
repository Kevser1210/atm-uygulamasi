## BANKA UYGULAMASİ
def hesap_olustur(sahibin_ismi):  # bakiye ve isim leri tutmasi için bir fonksiyon yazdık
    return {"sahibi":sahibin_ismi,"bakiye":0} # geri döndürmesi için
def deposit(hesap,miktar):
    if(miktar>0):
       hesap["bakiye"]+=miktar 
       print(f"{miktar} tl basarili bir sekilde yatirildi,bakiyeniz {hesap["bakiye"]} tl ") 
    else:
        print("yatirilicak miktar pozitif olmasi gerekir.")
def para_cekme(hesap,miktar):
    if(miktar>0):
        if(hesap["bakiye"]>miktar):
            hesap["bakiye"]-=miktar
            print(f"{miktar} tl basarili bir sekilde cekildi ,bakiyeniz{hesap["bakiye"]} tl")
        else:
          print("yetersiz bakiye")
    else:
        print("cekilecek miktar pozitif olmasi gerekir")
def bakiye_goster(hesap,miktar):
    print(f"{hesap["sahibi"]} guncel bakiyeniz {hesap["bakiye"]} tl")

print("bankamizin hesap uygulamasina hos geldiniz")
sahibi=input("hesap sahibinin adina girin:")
hesap=hesap_olustur(sahibi)

while True:
    print("\nsecenekler\n")
    print("1.para yatirma")
    print("2.para cekme")
    print("3.hesap görüntüleme")
    print("4.cikis")
    choice=int(input("secim yap (1-4)"))
    if(choice==1):
        miktar=float(input("yatirmak istediginiz miktari giriniz"))
        deposit(hesap,miktar)
    elif(choice==2):
        miktar=float(input("cekmek istediginiz miktara girin"))
        para_cekme(hesap,miktar)
    elif(choice==3):
        bakiye_goster(hesap,miktar)
    elif(choice==4):
        print("cikis yaptiniz .nice to meed you")
    else:
        print("gecersiz bir islem yaptiniz lutfen (1-4) arasinda bir sayi girin")

# 2. örnek
#### ATM uygulamasi
bakiye=1000
def secenekler():
    print("1.para yatirma")
    print("2.para cekme")
    print("3.bakiye goruntuleme")
    print("4.exit")
def para_yatirma(miktar):
    global bakiye
    miktar=int(input("ne kadar para yatirilicaksiniz"))
    print(f"{miktar} tl yatirildi")
    bakiye+=miktar
    print(f"{bakiye} toplam bakiyeniz")
def para_cekme(miktar):
    global bakiye
    miktar=int(input("cekilecek miktari giriniz"))
    if(miktar>bakiye):
        print("yetersiz bakiye")
    else:
      print(f"{miktar} tl para cekildi")
      bakiye-=miktar
      print(f"{bakiye} toplam bakiyeniz")
def bakiye_goruntuleme():
    global bakiye
    print(f"{bakiye} toplam bakiyeniz")
    
while True:   
    secenekler()
    secim=int(input("seciminize girin (1-4)"))
    if(secim==1):

        para_yatirma(bakiye)
    elif(secim==2):
        para_cekme(bakiye)
    elif(secim==3):
        bakiye_goruntuleme()
    elif(secim==4):
        print("cikis yaptiniz")
        break
    else:
        print("gecersiz bir islem yaptiniz lütfen tkr deneyiniz......")

    















