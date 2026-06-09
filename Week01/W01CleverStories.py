# In this activity, I added a new variable called title. The main idea is to connect the animal with the Clever's family. 
# So his littler brother is surprised with it and say a comic book hero name to the animal.
print()
print("Please enter the following:")
print()
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
title = input("comic book hero name: ")
print()

print("Your story is:")
print()
print('The other day, I was really in trouble. It all started when I saw a very'
        f' {adjective.lower()} {animal.lower()} {verb1.lower()} down the hallway.'
        f' "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2.lower()} over and over.'
        f' Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family.'
        f' My little brother said to the {animal.lower()}: "Go ahead, {title.upper()}!"'
    )