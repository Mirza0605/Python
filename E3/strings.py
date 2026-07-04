name = 'Mirza'
surname = 'Çelik'
age = 20

#print('My name is ' + name + ' ' + surname + ' and I am ' + age + ' years old.') => #bu şekilde hata verir çünkü str ile int birleşemez. Age kısmını '' bu şekilde yaarsak hata düzelir. Ya da print kısmındaki age i str(age) olarak yazarak hatayı düzeltebiliriz.

greeting = 'My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old.'
length = len(greeting)

# print(greeting)
# print(greeting[0])
# print(greeting[2])
# print(greeting[length-1])
#print(greeting[-1])
#print(greeting[2:5]) => #2den başla 5e kadar git.
#print(greeting[3:]) => #3ten başla sonuna kadar git.
#print(greeting[:16]) => #baştan başla 15e kadar git.
#print(greeting[2:40:2]) => #2den başla 40a kadar git ancak 2 karakterde 1 al.
