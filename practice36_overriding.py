# 매서드 오버라이딩

# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도2]"\
            .format(self.name, location, self.speed))


# 공격유닛
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed)  
        self.damage = damage

    def attack(self, location):    
        print("{0} :{1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 드랍쉽 : 공중 유닛, 수송기 . 마린/파이어뱃/탱크 등을 수송. 공격기능 x 

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))


#날 수 있는 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed): # 다중상속 AttackUnit/Flyable
        AttackUnit.__init__(self, name, 0, hp, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)        

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20) #    def __init__(self, name, hp, speed, damage): 

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3) #    def __init__(self, name, hp, damage, flying_speed)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")


