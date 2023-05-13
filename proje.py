class Sozluk:
    def __init__(self):
        with open('proje.txt', 'r') as dosya:
            satirlar = dosya.readlines()
        self.sozluk = {}
        for satir in satirlar:
            kelime, tanim = satir.strip().split(":")
            self.sozluk[kelime]=tanim
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

    def tanim_degistir(self):
        kelime = input("Lütfen tanımını değiştirmek istediğiniz kelimeyi giriniz:")
        kelime = kelime.capitalize()
        tanim = input("Lütfe yeni tanımı giriniz:")
        if kelime in self.sozluk:
             self.sozluk[kelime] = tanim
             print("Kelimenin tanımı güncellendi.")
        else:
             print("Aradığınız kelime bulunmadı.Bu kelimeyi sözlüğe ekleyip yeni tanım oluşturabilirsiniz.")
             self.sozluk[kelime] = tanim
             print("Kelime sözlüğe eklendi.")
        with open('proje.txt','w') as dosya:
            for key1 in self.sozluk.keys():
                dosya.write(f"{key1} : {self.sozluk[key1]}\n")

    def es_anlamli_kelime_ekle(self):
        kelime = input("Lütfen eş anlamlısını öğrenmek istediğiniz kelimeyi giriniz:")
        kelime = kelime.capitalize()
        es_anlam = input("Lütfen öğrenmek istediğiniz kelimenin eş anlamını giriniz:")
        if kelime in self.sozluk:
            self.sozluk[kelime].append(es_anlam)
            print("Eş anlamlı sözcük sözlüğe eklendi.")
        else:
            with open("es_anlamlilar.txt", "a") as f:
                 f.write(kelime + "," + es_anlam + "\n")
                 print("Yeni kelime ve eş anlamlısı dosyaya kaydedildi.")
            self.sozluk[kelime] = [es_anlam]
        
            
    def kelimeyi_deftere_ekle(self):
        kelime=input("Anlamını bilmediğiniz kelimeyi giriniz: ")
        anlam=input("Bilmediğiniz kelimenin anlamını giriniz: ")
        with open("defter.txt","a") as dosya:
            dosya.write(kelime+":"+anlam+"\n")
        


    def kelime_defterini_goster(self):
        with open("defter.txt","r") as dosya:
            satirlar=dosya.readlines()
            for satir in satirlar:
                kelime,anlam=satir.strip().split(":")
                print(kelime,":",anlam)
        
            
def main():
    sozluk=Sozluk()
    #sozluk.kelime_bilgi_goster()
    #sozluk.cumleEkle()
    #sozluk.yorumEkle()
    #sozluk.tanim_degistir()
    sozluk.es_anlamli_kelime_ekle()
    #sozluk.kelime_defterini_goster()
    #sozluk.kelimeyi_deftere_ekle()
    
main()
