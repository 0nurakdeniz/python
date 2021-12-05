""" Class and constructor"""

class Calisan:
    
    zam_orani=1.8
    counter =0
    
    def __init__(self,isim,soyisim,maas): # constructor
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@asd.com"
        
        Calisan.counter += 1
        
    def giveNameSurname(self):
        return self.isim+" "+self.soyisim
    
    def zam_yap(self):
        self.maas=self.maas + self.maas*self.zam_orani
        
isci1 = Calisan("ali" , "veli" ,100)

print(isci1.email)

print(isci1.giveNameSurname())

print("\n*****part2****")
"""class variables"""

calisan1 = Calisan("ali" , "veli" ,100)
print("ilk maas : ",calisan1.maas)

calisan1.zam_yap()
print("yeni maas : ",calisan1.maas)
print("Calısan sayısı: " , Calisan.counter)

calisan2 = Calisan("ayse" , "hatice" ,200)
print("Calısan sayısı: " , Calisan.counter)

calisan3 = Calisan("hatma" , "hayriye" ,300)
calisan4 = Calisan("civan" , "mert" ,400)

liste = [calisan1,calisan2,calisan3,calisan4]

print(liste)

max_maas=-1

for each in liste:
    if(each.maas>max_maas):
        max_maas=each.maas
        name=each.isim
        
print(max_maas , name)


######
"""
class A:

    global a

    a = 5

    def __init__(self,x = 4):

        self.x = x

    def sum(self):

        return a + self.x

x = A(5)

x.sum()"""

class A:
    global a
    a=5
    def __init__(self,x=4):
        self.x=x
        print("init icindeki x : ",self.x)
        
    def sum(self):
        print("sum içindeki a ve x: ",a,self.x)
        return a+self.x

x=A(5)
print(x.sum())




#%% syntax error
#print 9
#int 10.0
# %% exceptions

a=10
b ="2"
liste=[1,2,3]
print(sum(liste)) 
#print(a+b) #unsupported
#print(k) #not defined
# %%

k=10
zero=0

try:
    a=k/zero
except ZeroDivisionError:
    a=0

print(a)
# %%

"""
index error : 
list1=[1,2,3,4]
list1[15]

module not found error:
import numpyy

file not found error:
import pandas as pd
pd.read_csv("asd")

type error
"2" + 2

value error
int("asd")


"""

try:
    1/0
except:
    print("except")
else:
    print("else")
finally:
    print("done")

# %%
