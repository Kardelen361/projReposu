class Sozluk:
    def __init__(self):
        with open('proje.txt', 'r') as dosya:
            satirlar = dosya.readlines()
        self.sozluk = {}
        for satir in satirlar:
            try:
                kelime , tanim = satir.strip().split(":")
                self.sozluk[kelime]=tanim
            except ValueError:
                print("Sözlük dosyasindaki bazi satirlar yanliş biçimde.")
        self.kelime_defteri = []
    
    def cumleEkle(self):
        kelime = input("Hakkinda cumle eklemek istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime not in self.sozluk:
            print("Aradiginiz kelime bulunamadi!\n Eger kelimeyi sozluge eklemek istiyorsaniz kelime ekle kismina gidebilirsiniz.")
        else:
            with open('proje.txt','r') as dosya:
                satirlar=dosya.readlines()
            with open('proje.txt','w') as dosya:
                for satir in satirlar:
                    if kelime in satir:
                        cumle=input("Eklemek istediginiz cumleyi giriniz:")
                        dosya.write(satir.strip() + f",ornek cumle = {cumle}\n")
                        print(f"'{cumle}' cümlesi,{kelime} kelimesine eklendi.")   
                    else:
                        dosya.write(satir)
                    
    def yorumEkle(self):
        kelime = input("Hakkinda yorum eklemek istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime not in self.sozluk:
            print("Aradiginiz kelime bulunamadi!\n Eger kelimeyi sozluge eklemek istiyorsaniz kelime ekle kismina gidebilirsiniz.")
        else:
            with open('proje.txt','r') as dosya:
                satirlar=dosya.readlines()
            with open('proje.txt','w') as dosya:
                for satir in satirlar:
                    if kelime in satir:
                        yorum=input("Eklemek istediginiz yorumu giriniz:")
                        dosya.write(satir.strip() + f",yorum = {yorum}\n")
                        print(f"'{yorum}' yorumu,{kelime} kelimesine eklendi.")   
                    else:
                        dosya.write(satir)        
    
    def kelime_bilgi_goster(self):
        kelime=input("lutfen aratmak istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime in self.sozluk:
            print(f"{kelime} kelimesi için bilgiler:{self.sozluk[kelime]}")
        else:
            print("Kelime sozlukte bulunamadi!Kelimeyi sozluge eklemek isterseniz kelime ekle kisminda ekleyebilirsiniz.")

    def tanim_degistir(self):
<<<<<<< HEAD
        kelime = input("Lütfen tanımını değiştirmek istediğiniz kelimeyi giriniz:")
        kelime = kelime.capitalize()
        tanim = input("Lütfe yeni tanımı giriniz:")
        if kelime in self.sozluk:
=======
        kelime=input("Lutfen tanimini degistirmek istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        tanim=input("Lutfen yeni tanimi giriniz:")
        if kelime in self.sozluk.keys():
>>>>>>> 9a98b26c9017bc6ff612f8268159e5de8fcc36b5
             self.sozluk[kelime] = tanim
             print("Kelimenin tanımı güncellendi.")
        else:
             print("Aradığınız kelime bulunmadı.Bu kelimeyi sözlüğe ekleyip yeni tanım oluşturabilirsiniz.")
             self.sozluk[kelime] = tanim
             print("Kelime sözlüğe eklendi.")
        with open('proje.txt','w') as dosya:
            for key1 in self.sozluk.keys():
                dosya.write(f"{key1}:{self.sozluk[key1]}\n")

    def es_anlamli_kelime_ekle(self):
<<<<<<< HEAD
        kelime = input("Lütfen eş anlamlısını öğrenmek istediğiniz kelimeyi giriniz:")
=======
        kelime = input("Lütfen eş anlamlısını kaydetmek istediğiniz kelimeyi giriniz.")
>>>>>>> 9a98b26c9017bc6ff612f8268159e5de8fcc36b5
        kelime = kelime.capitalize()
        es_anlam = input("Lütfen kelimenin eş anlamlisini giriniz:")
        if kelime in self.sozluk:
            self.sozluk[kelime].append(es_anlam)
            print("Eş anlamlı sözcük sözlüğe eklendi.")
        else:
            with open("es_anlamlilar.txt", "a") as f:
                 f.write("kelimemiz:"+kelime + " , " +"es anlamlisi:"+es_anlam + "\n")
                 print("Yeni kelime ve eş anlamlısı dosyaya kaydedildi.")
<<<<<<< HEAD
            self.sozluk[kelime] = [es_anlam]
=======
>>>>>>> 9a98b26c9017bc6ff612f8268159e5de8fcc36b5
        
            
    def kelimeyi_deftere_ekle(self):
        kelime=input("Anlamını bilmediğiniz kelimeyi giriniz: ")
        anlam=input("Bilmediğiniz kelimenin anlamını giriniz: ")
        with open("defter.txt","a") as dosya:
            dosya.write(kelime+":"+anlam+"\n")
            print(f"{kelime} kelimesi ve anlami deftere eklendi!")
        
    def kelime_ekle(self):
        kelime = input("Eklemek istediğiniz kelimeyi giriniz: ")
        kelime = kelime.capitalize()
        anlam = input("Lütfen girdiğiniz kelimenin anlamını giriniz: ")
        if kelime not in self.sozluk:
            self.sozluk[kelime] = [anlam]
            with open('proje.txt', 'a') as dosya:
                dosya.write(f"\n{kelime}:{anlam}\n")
                print(f"{kelime} kelimesi sözlüğe eklendi.")
        else:
            print(f"{kelime} kelimesi zaten sözlükte mevcut.")

    def kelime_defterini_goster(self):
        print("Kelime defteri gosteriliyor..")
        with open("defter.txt","r") as dosya:
            satirlar=dosya.readlines()
            for satir in satirlar:
                kelime,anlam=satir.strip().split(":")
                print(kelime,":",anlam)
        
            
def main():
    sozluk=Sozluk()
<<<<<<< HEAD
    #sozluk.kelime_bilgi_goster()
    #sozluk.cumleEkle()
    #sozluk.yorumEkle()
    #sozluk.tanim_degistir()
    sozluk.es_anlamli_kelime_ekle()
    #sozluk.kelime_defterini_goster()
    #sozluk.kelimeyi_deftere_ekle()
=======
    print("""
    Sözlük
    1.Kelime ekleme
    2.Tanım değiştirme
    3.Eş anlam ekle
    4.Cümle ekle
    5.Yorum ekle
    6.Kelime defteri ekle
    7.Kelime defteri göster
    8.Kelime bilgi göster
    Çıkmak için "enter" a basın.""")

    while True:
        islem= input("İşlemi seçiniz:")
        if (islem==""):
            print("Siteden çıkış yapıldı.")
            break
        elif (islem=="1"):
            sozluk.kelime_ekle()
        elif (islem=="2"):
            sozluk.tanim_degistir()
        elif (islem=="3"):
            sozluk.es_anlamli_kelime_ekle()
        elif (islem=="4"):
            sozluk.cumleEkle()
        elif (islem=="5"):
            sozluk.yorumEkle()
        elif (islem=="6"):
            sozluk.kelimeyi_deftere_ekle()
        elif (islem=="7"):
            sozluk.kelime_defterini_goster()
        elif (islem=="8"):
            sozluk.kelime_bilgi_goster()
        else:
            pass
>>>>>>> 9a98b26c9017bc6ff612f8268159e5de8fcc36b5
    
main()
