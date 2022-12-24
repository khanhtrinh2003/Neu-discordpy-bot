import random

class DoanSo():
    l = []

    def __init__(self, s):
        self.s = s  
        DoanSo.l.append(random.randint(1, 100))
        
    def play(self):  

        if self.s == DoanSo.l[0]:
            DoanSo.l=[]
            return ('CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ')

        elif self.s > DoanSo.l[0]:
            return (f'SỐ ĐÓ BÉ HƠN {self.s}')
        else:
            return (f'SỐ ĐÓ LỚN HƠN {self.s}')

class Game_theory():
    l = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    computer_choices = ['Búa', 'Kéo', 'Bao']
    money = 100
    ind = 0

    def __init__(self, s, reset):
        self.reset = reset
        self.s = s  
        Game_theory.ind = random.randint(0,2)
        if reset == False:
            Game_theory.money += Game_theory.l[s][Game_theory.ind]
        else:
            Game_theory.money = 100 + Game_theory.l[s][Game_theory.ind]

    def play(self):
        return (f"Số tiền của bạn: {Game_theory.money}\n Bạn chơi : {Game_theory.computer_choices[self.s]}\n Máy chơi: {Game_theory.computer_choices[Game_theory.ind]}")

