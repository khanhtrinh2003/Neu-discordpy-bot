import random

class DoanSo():
    l = []
    buoc = 0

    def __init__(self, s):
        self.s = s  
        DoanSo.l.append(random.randint(1, 100))
        DoanSo.buoc += 1
        
    def play(self):  

        if self.s == DoanSo.l[0]:
            DoanSo.l=[]
            a = DoanSo.buoc
            DoanSo.buoc = 0
            return (f'CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ{self.s} sau {a} bước')

        elif self.s > DoanSo.l[0]:
            return (f'SỐ ĐÓ BÉ HƠN {self.s}')
        else:
            return (f'SỐ ĐÓ LỚN HƠN {self.s}')
