supported_sizes = ('Small','Medium','Large','small','medium','large','Big','big')

class animal_size:
    def __init__(self,size):
        self.size = size

    def __str__(self):
        if self.size in supported_sizes:

            return f'{self.size}'
        else:

            return f'Sorry, the given size is incompatible.'

    def __eq__(self,other):
        return self.size == other.size


other_size = animal_size('Big')
my_size = animal_size('Big')
print(my_size)
print(my_size == other_size)

class squid:
    def __init__(self,name,level,breed,age,size):
        self.name = name
        self.level = level
        self.breed = breed
        self.age = age
        self.size = size

    def make_sound(self):
        print(f'{self.name} made a {self.level} squishing noise.')

    def __str__(self):
        return f'{self.name} is a {self.breed} squid, {self.age} years old, {self.size} size, and they make {self.level} noises.'

    def __eq__(self,other):
        if self.breed == other.breed and self.size == other.size and self.age == other.age:
            return True
        else:
            return False

class goat:
    def __init__(self,name,level,breed,age,size):
        self.name = name
        self.level = level
        self.breed = breed
        self.age = age
        self.size = size

    def __str__(self):
        return f'{self.name} is a {self.breed} goat, {self.age} years old, {self.size} size, and they make {self.level} noises.'

    def __eq__(self, other):
        if (self.breed == other.breed
            and self.size == other.size
            and self.age == other.age):
            return True
        else:
            return False

    def make_sound(self):
        print(f'{self.name} made a {self.level} bleat.')

franky = goat('Franky','Ear-Shattering',"Screaming",42,my_size)
robin = squid("Robin","Calm","Giant",55,my_size)
animals =[franky,robin]

print(franky == robin)

print(franky)
print(robin)


for animal in animals:
    animal.make_sound()

