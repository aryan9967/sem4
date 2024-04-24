class animal:
    def sound(self):
        print("some sound")
        
class dog(animal):
    def sound(self):
        print("bark")
        
my_dog = dog()
my_dog.sound()

animal1 =animal()
animal1.sound()