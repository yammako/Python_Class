# 클래스 (스타크래프트 예시)
# 마린 : 공격 유닛으로 군인이고 총을 쏠 수 있음
name = "마린"   # 이름
hp = 40         # 체력
damage = 5      # 공격력
print("{0} 유닛이 생성되었습니다.".format(name))
print("채력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛 포를 쏠 수 있고 일반 모드 / 시즈 모드가 있음
tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("채력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 탱크가 하나 더 추가된다면 또 다시 탱크 관련 변수를 만들어 줘야 한다. 하지만 게임에서 탱크의 수는 매우 많기 때문에 이걸 다 써 줄 수 없다. 따라서 클래스가 필요하다.
# 연관성 있는 변수와 함수를 묶어 둔 집합이 클래스라 생각하면 된다.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ 객체를 생성하는 기본 함수
# marine3 = Unit("마린")        에러 발생
# marine3 = Unit("마린", 40)    에러 발생

# 멤버 변수 : 클래스에서 정의된 변수

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에서 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))     # 멤버 변수를 외부에서 사용 가능

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗는 것)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True         # 외부 변수를 각 객체에 추가할 수 있음. wraith1에는 clocking 변수가 없음.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

# 상속

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):                     # Unit class에서 name과 hp를 상속 받는다.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)       # 상속 받을 때는 __init__를 사용
        self.damage = damage        

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속
# 상속을 하는 클래스를 부모클래스, 상속을 받는 클래스를 자식클래스라 함. 여러 부모에게서 상속을 받는 것을 다중 상속이라 함.
# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 기능 없음.
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 50, 5, 6)
valkyrie.fly(valkyrie.name, "3시")