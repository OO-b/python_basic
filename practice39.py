# super 다중상속시

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()  # 다중상속일때 super를 쓰면 맨처음에 있는걸로 인식함

        #so, 다중상속 시 해당 클래스명을 명시해야함!
        Unit.__init__(self)
        Flyable.__init__(self) 



#드랍쉽
dropship = FlyableUnit()
