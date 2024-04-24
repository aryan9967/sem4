# class animal:
#     def sound(self):
#         print("some sound")

# class herbivores:
#     def eats(self):
#         print("grass")
        
# class cow(animal, herbivores):
#     def voice(self):
#         print("moo")
        
# my_cow = cow()
# my_cow.voice()
# my_cow.eats()
# my_cow.sound()

class animal:
    def sound(self):
        print("some sound")

class herbivores(animal):
    def eats(self):
        print("grass")
        
class cow(herbivores):
    def voice(self):
        print("moo")
        
new_cow = cow()
new_cow.voice()
new_cow.eats()
new_cow.sound()