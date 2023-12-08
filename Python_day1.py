#From Anvar Narzullayev Book (Dasturlash asoslar)
# ------------------------
# upper() / lower() - methods

# name = 'Nodirjon'
# surename = 'Murodjonov'
# full_name = f"{name} {surename}"  # - to comment like that press (Ctr+/)
#print(full_name)
#print(full_name.upper()) # it Uppers all the letters abc -> ABC
#print(full_name.lower()) # it lowers all the letters Abc -> abc
#----------------------------------
# title() / capitalize() - methods

# full_name = 'nodirjon murodjonov'
# print(full_name.title()) 
# print(full_name.capitalize())

# print(full_name.upper())
#------------------------------------
# lstrip(), rstrip(), strip() - methods

#lstrip() -> removes an empty space from left side (from beginnig of the text)
#rstrip() -> removes an empty space from right side (from ending of the text)
#strip() -> removes empty spaces from both sides 

# fruit = "       apple       "
# print(fruit)
# #lsrip 
# print("I love an " + fruit.lstrip() + " and it's delicious.")
# print("I love an " + fruit.rstrip() + " and it's delicious.")
# print("I love an " + fruit.strip() + " and it's delicious.")

# These methods will not change an original veraible but only shows us how it could be if we use these methods !
#-----------------------------
# Input() - method

# name = input('What is your name? ')
# print(f"Assalomu alaykum, {name}")

# name = input("What is your name? \n") # (\n) this method moves next words to next line (to bottom part in our case)
# print(f"Assalomu alaykum, {name.title()}")

#------------------------------
#Practise 1
# kocha = 'bog\'bon'
# mahalla = 'sag\'bon'
# tuman = 'bodomzor'
# viloyat = 'samarqand'

# print(f"{kocha.capitalize()} ko'chasi, {mahalla.capitalize()} mahallasi, {tuman.capitalize()} tumani, {viloyat.capitalize()} viloyati.")

#Practise 2
# kocha = input("Ko'changiz nomini kiriting: \n")
# mahalla = input("Mahallangiz nomini kiriting: \n")
# tuman = input("Tumaningiz nomini kiriting: \n")
# viloyat = input("Viloyatingiz nomini kiriting: \n")

# print(f"Siz {viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko'chasida turar ekansiz.")

#Practise 3
# kocha = input("Ko'changiz nomini kiriting: \n")
# mahalla = input("Mahallangiz nomini kiriting: \n")
# tuman = input("Tumaningiz nomini kiriting: \n")
# viloyat = input("Viloyatingiz nomini kiriting: \n")

# print(f"Siz {viloyat} viloyati,\n{mahalla} mahallasi,\n{tuman} tumani,\n{kocha} ko'chasida turar ekansiz.") # to execute every info from new line

#Practise 4
# kocha = input("Ko'changiz nomini kiriting: \n")
# mahalla = input("Mahallangiz nomini kiriting: \n")
# tuman = input("Tumaningiz nomini kiriting: \n")
# viloyat = input("Viloyatingiz nomini kiriting: \n")

# address = f"Siz {viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko'chasida turar ekansiz."
# print(address.title())
# print(address.upper())
# print(address.lower())
# print(address.capitalize())

a = input("Enter anything: ")
print(a.capitalize())
print(a.title())
print(a.upper())
print(a.lower())

# We could do more than 1 hour (64min) programming , we did it Alhamdulillah !



