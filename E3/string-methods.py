message = 'Hello There. My name is Mirza Çelik'

# message = message.upper() => Tüm harfleri büyük yapar.
# message = message.lower() => Tüm harfleri küçük yapar.
# message = message.title() => Her kelimenin ilk harfini büyük yapar.
# message = message.capitalize() => Sadece ilk harfini büyük yazar "Hello there. my name is mirza çelik" bu çıktıyı verir.
# message = message.strip() => baştaki boşluk gider.
# message = message.split() #=> karakter dizisi olarak çıktı verir."['Hello', 'There.', 'My', 'name', 'is', 'Mirza', 'Çelik' ]" bu çıktıyı verir.
# message = message.split('.') => Noktalardan ayırır.[' Hello There', ' My name is Mirza Çelik'] bu çıktıyı verir.
# message = '---'.join(message) => Her karakter arasına --- koyar.
# index = message.find('Mirza') => Aranan kelimenin ilk harfini çıktı olarak verir. 
# isFound = message.startswith('H') => H ile başlıyor mu anlamına gelir false ya da true çıktısı üretir. Boşluk ile başlama varsa false değeri üretir.
# isFound = message.endswith('k') => k ile bitiyor mu anlamına gelir. False ya da true çıktısı üretir
# message = message.replace('Mirza','Furkan') => Mirzayı Furkan olarak değiştirir.
# message = message.center(100) => Çıktıyı 100 karakterli bir container içine sığdırmış gibi düşün.
# message = message.center(50,'*') => Çıktıyı ortalar ve sağına soluna * ekler.

print(message)