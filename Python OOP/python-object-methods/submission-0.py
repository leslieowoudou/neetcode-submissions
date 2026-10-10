class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        self.hunger -=1
        print("Fluffy has been fed.")
        # and print a message about feeding the pet
        print(f"Fluffy's hunger level: {self.hunger}")

# Create a pet
my_pet = Pet("Fluffy")
my_pet.feed()
my_pet.feed()
my_pet.feed()
# TODO: Feed the pet three times
