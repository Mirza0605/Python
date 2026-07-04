name = 'Mirza'
surname = 'Çelik'
age = 20

# print('My name is {} {}'.format(name, surname))
# print('My name is {1} {0}'.format(name, surname)) => Çelik Mirza çıktısını verir.
# print('My nameis {s} {n}'.format(n=name,s=surname)) => Çelik Mirza çıktısını verir.
# print("My name is {} {} and I'm {} years old".format(name, surname, age))
# print("My name is {} {} and I'm {} years old".format(name, name, name)) => Tüm boşluklara Mirza gelir.

# result = 200 / 700
# print('the result is {}'.format(result)) => the result is 0.2857142857142857 bu çıktıyı verir.

# result = 200 / 700
# print('the result is {r:1.3}'.format(r=result)) => the result is 0.286 bu çıktıyı verir. 3 bilgisi virgülden sonra kaç basamak olacağını belirliyor. 1 kısmı ise is ile sayısı arasındaki birim boşluğunu belirler, 10 olsaydı 10 birimlik boşluk olacaktı.

# print(f"My name is {name} {surname} and I'm {age} years old.") => My name is Mirza Çelik and I'm 20 years old. bu çıktıyı verir. f işlemi basitleştirir.