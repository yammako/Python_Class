class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):                     # Unit class에서 name과 hp를 상속 받는다.
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)       # 상속 받을 때는 __init__를 사용
        self.damage = damage        

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 이동할 때 지상 유닛인지 공중 유닛인지 구분하고 move, fly를 사용해야 하므로 번거롭다. 이때 오버라이딩을 사용한다.
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      # 지상 스피드는 0으로 설정
        Flyable.__init__(self, flying_speed)

    def move(self, location):                               # move 함수를 만들어 fly 함수를 호출하므로써 오버라이딩 실행
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass                                        # 아무런 실행 없이 넘어가는 명령

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛 생성 가능
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass                    # game_over를 호출하면 pass 때문에 아무런 기능을 하지 않음.

game_start()
game_over()