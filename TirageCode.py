from random import shuffle

#COMPTENEUR
lst = []

# COMPTER DE 1 A 99
for x in range(1,100):
# GROUPER DANS LE COMPTENEUR    
    lst.append(x)
#REMUER
    shuffle(lst)
print("And the lucky numbers are")

#TIRER JUSTE 6 NOMBRE DE 1 A 99
print(*lst[0:6], sep="\n")
print("You're the Winner!")
print("Raphy GIT!")

#Trying GIT & GitHub
