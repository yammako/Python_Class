class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()        # Unit class만 상속됨

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()        # Flyable class만 상속됨

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()        # Unit class, Flyable class 모두 상속됨

# super는 하나의 상속만 가능하므로 다중 상속을 할 때는 super를 사용하면 안됨.
