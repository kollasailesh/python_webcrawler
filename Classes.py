__author__ = 'SAILESH'

class Enenmy:
    life = 3
    def attack(self):
        self.life -= 1
        print("ouch!")
    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life), "Life left")
enemy1 = Enenmy()
enemy1.attack()
enemy1.checkLife()