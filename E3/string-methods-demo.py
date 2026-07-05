website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

# result = ' Hello World'.strip()
# result = ' Hello World'.lstrip()
# result = ' Hello World'.rstrip()

# print(result)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

# result = 'www.sadikturan.com'.strip('w.moc') => Tekrar eden harfleri 1 kere yazsan okey.
# print(result)

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

# result = course.lower()
# print(result)

# 4- 'website' içinde kaç tane a karakteri vardır? (count('a'))

# result = website.count('a')
# result = website.count('www',0,10) => 0 ile 10 arasında www kaç tane var demek
# print(result)

# 5- 'website' www ile başlayıp com ile bitiyor mu?

# result = website.startswith('www')
# print(result)

# 6- 'website' içinde '.com' ifadesi var mı?

# result = website.find('.com')
# result = website.index('com')
# print(result)

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

# result = course.isalpha() => flase
# result = 'Hello'.isalpha() => true
# result = course.isdigit() => rakam mı
# print(result)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

# result = 'Contents'.center(50,'*')
# result = 'Contents'.ljust(50,'*') => ifadeyi sola yaslar yıldızları sağına ekler
# result = 'Contents'.rjust(50,'*') => ifadeyi sağına yaslar yıldızları soluna ekler
# print(result)

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' değiştirin.

# result = course.replace(' ','-')
# result = course.replace(' ','-',5) => sadece 5 tane - koyar
# print(result)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

# result = 'Hello World'.replace('World','There')
# print(result)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

# result = course.split(' ')
# print(result)