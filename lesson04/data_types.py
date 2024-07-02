

#String data type
#literal ssignment
first = "Dave"
last = "Gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str)) #bir string örneği mi?


# construction function
pizza = str("pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last

fullname += "!"

# Casting a number to a string
decade = str(1980)

statement = "I like rock music from the " + decade +"s."

#Multiple Line

multiline = '''
Hey, how are you?

I was just checking in.
                            All good?
'''

print(multiline)

#Escaping special characters

sentence = "I'm" #şekinde yazılır yada
sentence = 'I\'m back at work\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods, method are funtion
print(first)

print(first.lower())
print(first.upper())
print(first)

multiline.title() #ilk harfi büyük harf yapar
multiline.replace("good", "ok")
len(multiline) #karakter sayısı

len(multiline.strip()) #baştaki ve sondaki boşlukları siler
len(multiline.lstrip()) #soldaki boşluklar
len(multiline.rstrip()) #sağdaki boşluklar

print("")
#Build a menu
title = "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheesecake".ljust(16,".") + "$4".rjust(4))

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data

print(first.startswith("D"))
print(first.endswith("Z"))

#Boolean data type
myvalue = True #False bool(False)
print(isinstance(myvalue, bool))

# Numeric data types

#integer
price  = 100
best_price = int(80)
print(isinstance(best_price, int))

#float type

gpa = 3.28

#complex type

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Build-in function s for numbers

print(abs(gpa))
print(round(gpa)) #en yakın yere yuvarlama
print(round(gpa,1)) # virgülden sonra kaç basamak olacak

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Cascading a string to a number
zipcode = "10001"
zip_value = int(zipcode)

#Error if you atempt tı cast incorrect data
#zip_value = int("Newyork")


