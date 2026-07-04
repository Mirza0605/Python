website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

# result = len(course)
# length = len(website)
# print(result)

# 2- 'website' içinden www karakterlerini alın.

# result = website[7:10]
# print(result)

# 3- 'website' içinden com karakterlerini alın.

# result = website[22:25]
# result = website[length-3:length]
# print(result)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

# result = course[0:15] => ilk 15
# result = course[:15] => ilk 15
# result = course[-15:] => son 15
# print(result)

# 5- 'course' ifadesindeki karakterli tersten yazdırın.

# result = course[::-1]
# print(result)

# s = '12345' * 5
# print(s) => 12345i 5 kere yan yana yazar.

# s = '12345' * 5
# print(s[::5]) => 5 karakterde bir al. Çıktısı 11111

name, surname, age, job = 'Mirza','Çelik', 20, 'mühendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
    # 'Benim adım Mirza Çelik, Yaşım 20 ve mesleğim mühendis.'

#result = "Benim adım" + name + " " + surname + ", Yaşım " + str(age) + " ve mesleğim mühendis." 
#result = 'Benim adım {} {}, Yaşım {} ve mesleğim {}.'.format(name,surname,age,job)
# result = f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.'
# print(result)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değişirin.

#s = 'Hello world'
#s = s[0:6] + 'W' + s[-4:]
#print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

result = 'abc' * 3
print(result)