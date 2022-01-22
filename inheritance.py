class Animals:
    alive = True


class Giraffe(Animals):
    def twigs(self):
        print("Eats twigs from trees")


giraffe = Giraffe()
giraffe.twigs()
print(giraffe.alive)
