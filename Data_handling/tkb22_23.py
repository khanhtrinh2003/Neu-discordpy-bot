import pandas as pd
import numpy as np

# Other function
def remove_three_last_letter(x):
    return x[:-3]

def lop(x):
    return x.split('.')[1]

def khoa(x):
    return x.split('.')[0]
# Handle data    
sheet_id = "1iUYz-EdeGfwCQ5X6E9_hRHMxaPOClxgVlz28yl_IEYI"
data1 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv", header=1)
data1.dropna(inplace=True)
data1 = data1[data1['Tình Trạng']!='Hủy']
data1["Môn học"]=data1["Tên HP"].map(remove_three_last_letter)
data1["Khoa"]= data1["Mã Lớp"].map(khoa)
data1["Lop"]= data1["Mã Lớp"].map(lop)


def room(days, period, building, floors):
    l1 = np.array(data1["Thời Khóa Biểu"][data1['Thời Khóa Biểu'].str.startswith(days+' '+period)==True]).reshape(1,-1).tolist()
    floor = building+'-'+floors
    print
    #Get new data follow by floor
    l=[]

    # Check and take information from data by floor
    for i in range(0,len(l1[0])):
        if floor in str(l1[0][i]):
            l.append(l1[0][i])

    #sort floor
    l = sorted(l)
    res = np.array(l[:15]).reshape(-1,1)
    return res

def hoc_ke(mon_hoc):
    lmon =[]
    mon_hocs=sorted(list(set(data1["Môn học"].tolist())))
    for i in range(0,len(mon_hocs)):
        if mon_hoc in str(mon_hocs[i]):
            lmon.append(mon_hocs[i])
    return np.array(data1[(data1["Môn học"].isin(lmon))][["Tên HP", "Thời Khóa Biểu", "Mã Lớp"]][:10]).reshape(-1,3)           


