

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
