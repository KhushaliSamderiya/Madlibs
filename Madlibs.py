# #Decalring a variable
# youtuber = "Khushali"

# #Three ways of doing string concatenation

# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

# adj = input("Adjectives: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Your role model: ")

# Madlib = f"Computer programming is so {adj}! It makes so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# print(Madlib)

topic = input("Choose a topic. Enter 'A' for Adventure and 'P' Pogramming ")

a = 'A'
p = 'P'


if topic == a:
 adj = input("Adjectives: ")
 verb1 = input("Verb: ")
 verb2 = input("Verb: ")
 famous_person = input("Your role model: ")

 Adv =  f"Adventure programming is so {adj}! It makes so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

 print(Adv)


elif topic == p:
 adj = input("Adjectives: ")
 verb1 = input("Verb: ")
 verb2 = input("Verb: ")
 famous_person = input("Your role model: ")

 Program =  f"Computer programming is so {adj}! It makes so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

 print(Program)

else: 
 print("invalid")