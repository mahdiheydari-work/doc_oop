class dog:
    def make_sound(self):
        print("bark")
class cat:
    def make_sound(self):
        print("meow")
def make_sound(obj):
    obj.make_sound()

my_cat = cat()
my_dog = dog()

make_sound(my_cat)
make_sound(my_dog)