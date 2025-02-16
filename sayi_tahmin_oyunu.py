import random
sayi = random.randint(1,100)
tur  =0
kullanici_verisi =0

while True:
  kullanici_verisi = input("1-100 arasında bir sayı giriniz: ")
  tur +=1
  if(kullanici_verisi == "q"):
    print("Oyunu İptal Ettiniz")
    break
  else:
    kullanici_verisi = int(kullanici_verisi)
    if(kullanici_verisi < 1 or kullanici_verisi > 100):
      print("Lütfen 1-100 arasında bir sayı giriniz")
      continue
    elif(kullanici_verisi > sayi):
      print("Daha Küçük Bir Sayı Giriniz")
    elif(kullanici_verisi < sayi):
      print("Daha Büyük Bir Sayı Giriniz")
    else:
      print(f"Tebrikler {tur}. Denemede Doğru Bildiniz")
      break