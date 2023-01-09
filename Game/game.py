import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Peo1 = ["S1", "N1"]
Peo2 = ["S2", "N2"]
payoff2 = [[-1, 1],[1, -1]]

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
class Infor():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def ER(self):
        EN = (2*self.p1-1)*(1-2*self.p2)
        return EN
    def Var(self):
        E=-2*self.p1+1
        V = (E**2+(4*self.p1-2)*E+1)*(self.p2**2+(1-self.p2)**2-2*self.p2*(1-self.p2))
        return V

class ve_do_thi():
    nums = 10000
    p10 = np.random.rand(nums)
    p20 = np.random.rand(nums)
    def __init__(self, p1):
        self.p1=p1
    
    def chien_luoc(self):
        if self.p1<0.5:
            e = "p2=1"
        elif self.p1>0.5:
            e = "p2=0"
        else:
            e = "Bất kể chiến lược nào cũng được"
        return (f"Người 1: {self.p1}\nChiến lược tối ưu cho người 2: {e}")
        
    def minh_hoa(self):
        fig = plt.figure()
        a= Infor(ve_do_thi.p10,ve_do_thi.p20)
        b = Infor(self.p1,ve_do_thi.p20)
        c = Infor(self.p1,0)
        d = Infor(self.p1,1)
        
        m= (b.ER()-b.Var()).tolist()
        p2 =ve_do_thi.p20[m.index(np.max(m))]
        e = Infor(self.p1, p2)   

        plt.scatter(a.Var(), a.ER())
        plt.scatter(b.Var(), b.ER(), color="pink")
        plt.scatter(c.Var(), c.ER(), color="yellow")
        plt.scatter(d.Var(), d.ER(), color="red")
        plt.scatter(e.Var(), e.ER(), color="green")
        plt.xlabel("var(p\u2082S\u2082+(1-p\u2082)S\u2082)")
        plt.ylabel("E(p\u2082S\u2082+(1-p\u2082)S\u2082)")
        return fig

class Kiem_dinh():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def mat_do_loi_nhuan(self):
        u1 =[]
        u2 = []
        u3 = []
        for i in range(1000):
            n1 = random.choices(Peo1, weights=[self.p1,1-self.p1], k=1000)
            n2 = random.choices(Peo2, weights=[self.p2,1-self.p2], k=1000)
            s1 = list(map(encode, n1))
            s2 = list(map(encode, n2))
            s3 = [1]*1000
            s4 = [0]*1000

            chien_luoc = list(map(to_li,list(zip(s1,s2))))
            chien_luoc1 = list(map(to_li,list(zip(s1,s3))))
            chien_luoc2 = list(map(to_li,list(zip(s1,s4))))
            u1.append(sum(list(map(thu_hoach2, chien_luoc))))
            u2.append(sum(list(map(thu_hoach2, chien_luoc1))))
            u3.append(sum(list(map(thu_hoach2, chien_luoc2))))
        
        u = pd.DataFrame({"Chiến lược bạn chọn": u1,"Chiến lược tối ưu": u2,"Chiến lược tối ưu ": u3})
        
        fig, ax = plt.subplots(1,1)
               
        if self.p1 <= 0.5:
            u["Chiến lược bạn chọn"].plot(kind='density')
            u["Chiến lược tối ưu "].plot(kind='density')
            
        else:
            u["Chiến lược bạn chọn"].plot(kind='density')
            u["Chiến lược tối ưu"].plot(kind='density')

        plt.legend()
        plt.xlabel("Số tiền nhận được")
        return fig


class Game_theo(Infor, ve_do_thi, Kiem_dinh):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)

def encode(s):
    if s == "N1" or s == "N2":
        return 1
    else:
        return 0

def to_li(e):
    return list(e)

def thu_hoach2(s):
    return payoff2[s[0]][s[1]]