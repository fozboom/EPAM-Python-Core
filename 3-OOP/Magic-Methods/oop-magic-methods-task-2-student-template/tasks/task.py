class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} bird can fly and walk"

    def walk(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can walk and fly"

    def eat(self):
        return f"It eats mostly {self.ration}"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can swim"

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


if __name__ == "__main__":
    b = Bird("Any")
    print(b.walk())

    p = NonFlyingBird("Penguin", "fish")
    print(p.swim())

    try:
        print(p.fly())
    except AttributeError as e:
        print(e)

    print(p.eat())

    c = FlyingBird("Canary")
    print(str(c))
    print(c.eat())

    s = SuperBird("Gull")
    print(str(s))
    print(s.eat())
