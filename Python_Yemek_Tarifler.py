class islemler :
    def tarif_ekle(self) :
        tarif_isim = input("Yemek Adı : ")
        tarif.append(tarif_isim)
        while True :  
            tarifAdimlari = input("Tarif Adımları Malzeme Ekleyin:(Adımlar Bittiyse - Giriniz) : ")
            if tarifAdimlari == "-" :
                tarifler.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarifAdimlari)
            

    def listele(self) :
        sayi = len(tarifler)
        print("Tüm Tarifler")    
        for adim in tarif :
                print(adim)



        
def menu() :
    while True :
        print("\nYeni tarif eklemek için : ekle\nVar olan tarifleri listelemek için : tarifler\nÇıkış yapmak için : cikis ")
        secim = input("yapmak istediğiniz işlem numarasını giriniz : ")
        islem = islemler()
        if secim == "ekle" :
            islem.tarif_ekle()
        elif secim == "tarifler" :
            islem.listele()
        elif secim == "cikis" :
            exit(0)
        else :
            print("Hatalı Seçim Lütfen Yapacağınız Işlemi Tekrar Seçiniz")



tarifler = []
tarif = []

menu()

