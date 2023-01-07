import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns
import pandas as pd

Peo1 = ["S1", "N1"]
Peo2 = ["S2", "N2"]
payoff2 = [[-1, 1],[1, -1]]

def encode(s):
    if s == "N1" or s == "N2":
        return 1
    else:
        return 0

def to_li(e):
    return list(e)

def thu_hoach2(s):
    return payoff2[s[0]][s[1]]


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
        b = Infor(self.p1,ve_do_thi.p20)
        if self.p1<0.5:
            e = 1
        elif self.p1>0.5:
            e = 0
        else:
            e = "Bất kể chiến lược nào cũng được"
        return (f"Người 1: {self.p1}\nNgười 2: {e}")
        
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
        plt.xlabel("var(p2S2+(1-p2)S2)")
        plt.ylabel("E(p2S2+(1-p2)S2)")
        return fig

class Kiem_dinh():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def mat_do_loi_nhuan(self):
        u1 =[]
        u2 = []
        for i in range(1000):
            n1 = random.choices(Peo1, weights=[self.p1,1-self.p1], k=1000)
            n2 = random.choices(Peo2, weights=[self.p2,1-self.p2], k=1000)
            s1 = list(map(encode, n1))
            s2 = list(map(encode, n2))

            chien_luoc = list(map(to_li,list(zip(s1,s2))))
            u1.append(sum(list(map(thu_hoach2, chien_luoc))))
        n2 = []
        s2 = []
        if self.p1 >0.5:
            for i in range(1000):
                n1 = random.choices(Peo1, weights=[self.p1,1-self.p1], k=1000)
                n2 = random.choices(Peo2, weights=[0,1], k=1000)
                s2 = list(map(encode, n2))
                s1 = list(map(encode, n1))
                chien_luoc = list(map(to_li,list(zip(s1,s2))))
                u2.append(sum(list(map(thu_hoach2, chien_luoc))))              
        
        elif self.p1 <=0.5:
            for i in range(1000):
                n1 = random.choices(Peo1, weights=[self.p1,1-self.p1], k=1000)
                n2 = random.choices(Peo2, weights=[1,0], k=1000)
                s2 = list(map(encode, n2))
                s1 = list(map(encode, n1))
                chien_luoc = list(map(to_li,list(zip(s1,s2))))
                u2.append(sum(list(map(thu_hoach2, chien_luoc))))              
        u = pd.DataFrame({"Chiến lược bạn chọn": u1,"Chiến lược tối ưu": u2})
        fig, ax = plt.subplots(1,1)
        for s in u.columns:
            u[s].plot(kind='density')
        plt.legend()
        plt.xlabel("Số tiền nhận được")
        return fig


class Game_theo(Infor, ve_do_thi, Kiem_dinh):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)
