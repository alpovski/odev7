# 2d arrayli ödev 7 dosyası

def tablo_yazdir(iki_boyutlu_liste, sporcu_say, atis_say):
    KAC_ADET_PUAN_TURU_VAR = 11
    puantop = 0
    puanlar = ["10 P", " 9 P", " 8 P", " 7 P", " 6 P",
               " 5 P", " 4 P", " 3 P", " 2 P", " 1 P", " 0 P"]
    print("Okçu Kayıt No ", end="")
    for puan_turu in puanlar:
        print(f"{puan_turu:5} ", end="")
    print("Toplam Puan")
    print("------------- ", end="")
    for i in range(KAC_ADET_PUAN_TURU_VAR):
        print("----- ", end="")
    print("-----------")
    sutun_top = [0] * KAC_ADET_PUAN_TURU_VAR
    sutun_puan_top = [0] * KAC_ADET_PUAN_TURU_VAR
    for sporcu in range(sporcu_say):
        print(f"{sporcu + 1:3}          ", end="")
        for puan_no in range(KAC_ADET_PUAN_TURU_VAR):
            print(f"{iki_boyutlu_liste[sporcu][puan_no]:5} ", end="")
            sutun_top[puan_no] += iki_boyutlu_liste[sporcu][puan_no]
            sutun_puan_top[puan_no] += iki_boyutlu_liste[sporcu][puan_no] * (KAC_ADET_PUAN_TURU_VAR-puan_no-1)
            puantop += iki_boyutlu_liste[sporcu][puan_no] * (KAC_ADET_PUAN_TURU_VAR-puan_no-1)
        print(f"  {puantop}")
        puantop = 0
    print("Toplam     ", end="")
    for puan_no in range(KAC_ADET_PUAN_TURU_VAR):
        print(f" %{sutun_top[puan_no]*10/atis_say:3} ", end="")
    print(f"{sum(sutun_puan_top):3}   ")


def ruzgar_tablosu(ruzgarDict):
    toplam = 0
    try:
        for i in ruzgarDict:
            toplam += ruzgarDict[i]
        print(f"Rüzgar Adı       Iska Atış Oranı(%)")
        print(f"----------       ------------------")
        for key, val in ruzgarDict.items():
            print(f"{key:10}   %{int(ruzgarDict[key]) * 100 / toplam}")
    except ZeroDivisionError:
        for key, val in ruzgarDict.items():
            print(f"{key:10}       %0")
        print("Yetersiz veri olduğundan dolayı sıfıra bölünme hatası çıkmıştır. Bunun yerine %0 yazıldı.")


def main():
    ruzgarDict = {"Yıldız": 0, "Poyraz": 0, "Gündoğusu": 0, "Keşişleme": 0, "Kıble": 0, "Lodos": 0, "Günbatısı": 0,
                  "Karayel": 0}
    MIN_SPORCU_SAY = 10
    KAC_ADET_PUAN_TURU_VAR = 11
    try:
        sporcu_say = int(input("Sporcu sayısı giriniz(10'dan fazla): "))
        if sporcu_say < MIN_SPORCU_SAY:
            print(f"Sporcu sayısı {MIN_SPORCU_SAY}'dan büyük olmalıdır.")
            sporcu_say = int(input("Sporcu sayısı giriniz(10'dan fazla): "))
    except ValueError:
        print("Lütfen sayı giriniz. ")
        sporcu_say = int(input("Sporcu sayısı giriniz(10'dan fazla): "))
    atis_say = int(input("Atış sayısı giriniz: "))
    tum_liste = []
    for i in range(sporcu_say):
        bir_sporcu_puan_list = [0] * KAC_ADET_PUAN_TURU_VAR
        tum_liste.append(bir_sporcu_puan_list)
    for sporcu_no in range(sporcu_say):
        for atis_no in range(1, atis_say + 1):
            try:
                atis = int(input(f"{sporcu_no + 1}. sporcunun {atis_no}. atışını giriniz(0-10): "))
                while not 0 <= atis <= 10:
                    print("Lütfen verilen parametreler arasında değer giriniz.")
                    atis = int(input(f"{sporcu_no + 1}. sporcunun {atis_no}. atışını giriniz(0-10): "))
            except ValueError:
                print("Lütfen bir sayı giriniz.")
                atis = int(input(f"{sporcu_no + 1}. sporcunun {atis_no}. atışını giriniz(0-10): "))
            tum_liste[sporcu_no][KAC_ADET_PUAN_TURU_VAR-atis-1] += 1
            if atis == 0:
                ruzgar_turu = input("Atışını kaçırdığında olan rüzgarın türünü giriniz: ")
                while ruzgar_turu not in ruzgarDict:
                    ruzgar_turu = input("Atışını kaçırdığında olan rüzgarın türünü giriniz: ")
                ruzgarDict[ruzgar_turu] += 1
    tablo_yazdir(tum_liste, sporcu_say, atis_say)
    ruzgar_tablosu(ruzgarDict)


main()
