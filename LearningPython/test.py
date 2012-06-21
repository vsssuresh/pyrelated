print 01100
def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'
do_twice(print_spam)    

S = set((2, 3, 5, 7, 11, 13))
for i in S:
    print i
    
class Duck:
    def quack(self):
        print("Quaaaaaack!")
    def feathers(self):
        print("The duck has white and gray feathers.")
        
 
class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")
 
def in_the_forest(duck):
    duck.quack()
    duck.feathers()
 
def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
 
game()  

# Speaking pets in Python:
class Pet:
        def speak(self): pass
class Cat(Pet):
        def speak(self):
            print "meow!"
class Dog(Pet):
        def speak(self):
            print "woof!"
def command(pet):
        pet.speak()
pets = [ Cat(), Dog() ]
for pet in pets:
        command(pet)
 
        
        