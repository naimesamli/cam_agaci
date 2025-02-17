def cam_agaci_ciz():
    while True:
        try:
            satir = int(input("Kaç satırlık çam ağacı istiyorsunuz? "))
            if satir <= 0:
                print("Lütfen pozitif bir sayı girin!")
                continue
            break
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
    
    max_bosluk = satir + 5
    
    for i in range(satir):
        yildiz = i + 1  
        bosluk = max_bosluk - i
        print(" " * bosluk + "*" * yildiz)

cam_agaci_ciz()