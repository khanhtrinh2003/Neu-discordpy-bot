import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Peo1 = ["C", "B"]
Peo2 = ["C", "B"]
payoff1 = [[2, 0],[0,1]]
payoff2 = [[1, 0],[0, 2]]


#Game Doan so
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

# Game theory
Peo1 = ["C", "B"]
Peo2 = ["C", "B"]
payoff1 = [[2, 0],[0,1]]
payoff2 = [[1, 0],[0, 2]]
def encode(s):
    if s == "B":
        return 1
    else:
        return 0

def to_li(e):
    return list(e)

def thu_hoach1(s):
    return payoff1[s[0]][s[1]]

def thu_hoach2(s):
    return payoff2[s[0]][s[1]]

class Kiem_dinh():
    dem =0
    cl = []
    ten = []

    def __init__(self, p, name):
        self.p = p
        self.name=name
        Kiem_dinh.dem += 1
        Kiem_dinh.cl.append(self.p)
        Kiem_dinh.ten.append(name)        
        if Kiem_dinh.dem == 3:
            Kiem_dinh.dem = 1
            Kiem_dinh.ten = Kiem_dinh.ten[2::]
            Kiem_dinh.cl = Kiem_dinh.cl[2::]

    def mat_do_loi_nhuan(self):
        if Kiem_dinh.dem == 2:
            u1 =[]
            u2 = []
        
            for i in range(1000):
                n1 = random.choices(Peo1, weights=[Kiem_dinh.cl[0],1-Kiem_dinh.cl[0]], k=1000)
                n2 = random.choices(Peo2, weights=[Kiem_dinh.cl[1],1-Kiem_dinh.cl[1]], k=1000)
                s1 = list(map(encode, n1))
                s2 = list(map(encode, n2))

                chien_luoc = list(map(to_li,list(zip(s1,s2))))

                u1.append(sum(list(map(thu_hoach1, chien_luoc))))
                u2.append(sum(list(map(thu_hoach2, chien_luoc))))
                        
            u = pd.DataFrame({f"Lợi ích của {Kiem_dinh.ten[0]}": u1,f"Lợi ích của {Kiem_dinh.ten[1]} ": u2})
            
            fig= plt.subplots(1,1)
            u[f"Lợi ích của {Kiem_dinh.ten[0]}"].plot(kind='density')
            u[f"Lợi ích của {Kiem_dinh.ten[1]} "].plot(kind='density')
            plt.legend()
            plt.xlabel("Lợi ích thu được được")
            plt.savefig(fname='test')
            return fig
        else: 
            return "Đã ghi nhận dữ liệu"


class Game_theo(Kiem_dinh):
    def __init__(self, p, ten):
        super().__init__(p, ten)

def encode(s):
    if s == "B":
        return 1
    else:
        return 0

def to_li(e):
    return list(e)

def thu_hoach1(s):
    return payoff1[s[0]][s[1]]

def thu_hoach2(s):
    return payoff2[s[0]][s[1]]
