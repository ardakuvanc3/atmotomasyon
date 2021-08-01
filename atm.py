#Belirli bir şifre ve kullanıcı adı ile sisteme giriş yapılıyor
#Kullanıcıya 4 işlem hakkı veriliyor
#Para çekme, yatırma, hesap bilgileri ve kart iade
#kullanici 2000 tl ile başlıyor



sifre=2308
gr_sifre=input("Lütfen Sifreyi Giriniz : ")

if int(gr_sifre) == int(sifre) :
       print("\n*****ATM'YE HOSGELDINIZ*****\n")
       
else : 
       print("Şifre Yanlış Çıkış Yapılıyor...")
       exit()

sahip_olunan_para = 2000

seçim = input("ATM'ye Hoş Geldiniz! İşlem Yapmak İçin 's', ATM'den çıkmak için 'a' tuşuna basınız: ")

if seçim == "s":
    while True:
        islem = int(input("""       
        İşlemler 
      ------------
      1-Para Çekme
      2-Para Yatırma
      3-Hesap Bilgileri
      4-Kart iade
      Yapmak istediğiniz işlemi giriniz: """))  
        
        if islem == 1:
            çekilmek_istenilen_para = int(input("Çekmek istediğiniz tutarı giriniz: "))

            if sahip_olunan_para < çekilmek_istenilen_para:
                print("İşlem Geçersiz! Bakiyeniz Yetersiz")
            else:
                sahip_olunan_para -= çekilmek_istenilen_para
                print("Para Çekildi Mevcut Bakiye: {}".format(sahip_olunan_para))
      
        if islem == 2:
            yatırılmak_istenilen_para = int(input("Yatırmak İstediğiniz Tutarı Giriniz: "))
            sahip_olunan_para += yatırılmak_istenilen_para
            print("Paranız Yatırıldı Sahip Olunan Hesap Bakiyesi: {}".format(sahip_olunan_para))
     
        if islem == 3:
            print("Hesap Bilgileriniz\n******************\nHesap Sahibi: Arda Kuvanç\nHesap İBAN NO: TR80 XXX XXXX\nSahip Olunan Para Miktarı: {}\n******************".format(sahip_olunan_para))
      
        if islem ==4:
            print("Kartınız İade Edildi, İyi Günler...")
            break
else:
    print("ATM'den ayrıldınız")
