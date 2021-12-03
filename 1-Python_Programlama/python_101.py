"""         variable            """

#%%
print('********cell 1********')
msg='Hello World' #string
print(msg)
var1=10 #integer
var2=15
x=var1+var2
print(x)
#%%
print('********cell 2********')
s = "bugun hava yagmurlu"
variable_type=type(s)
print(variable_type,s)
#variable_type
#var1 not defined
uzunluk=len(s)
print(uzunluk)
print(s[0])

# %%
print('********cell 3********')
float1=10.6
print(float1)
print(round(float1))
print(int(float1))
# %% user defined functions
print('********cell 4********')
def func1(var1,var2):
    output=(((var1+var2)*50)/100)*var1/var2
    return output

print(func1(20,50))
# %% default and flexible functions
print('********cell 5********')
def cember_cevre(r,pi=3.14):
    return(2*r*pi)

print(cember_cevre(2))


def hesapla(boy,kilo,*args):
    print(args)
    return print((boy+kilo)*args[0])

hesapla(1,2,5,10)

# %%
print('********cell 6********')
yas=25
name="onur"
akdeniz="akdeniz"

def fun3(a,b,*args,d=42):
    
    return print("isim:",a,"yas:",b,"ayak no:",d)
    
fun3(name,yas)
# %% lambda func
print('********cell 7********')


sonuc= lambda x:x*x
print(sonuc(3))
# %% list
print('********cell 8********')

list1=[1,2,3,4,5]
print(type(list1))
print(list1)

list2= ["ptesi","sali","cars","pers","cuma","ctesi","pazar"]
print(type(list2))
print(list2[-1])

print(list2[0:-3])

print(dir(list))

list1.append(6)
print(list1)

#tuple

t=(1,2,3,4,5,6,3)
print(t[2])
print(dir(tuple))
print(help(tuple.count))
print(t.count(2))
print(t.count(3))


# %% dictionary
print('********cell 9********')

dictionary={"ali":32,"veli":42,"ayşe":13}
print(dictionary)

print(dictionary["ali"])
print((dictionary.keys()))
print(dictionary.values())

# %% conditionals
print('********cell 10********')

var1=30
var2=20

if(var1>var2):
    print("var1 büyük")
elif(var1==var2):
    print("eşitler")
else:
    print("v1 kucuk")
    
liste=[1,2,3,4,5]

val=3

if val in liste:
    print("{} var".format(val))
else:
    print("{} yok".format(val))
    
    
keys = dictionary.keys()

if "ali" in keys:
    print("ali var")
else:
    print("ali yok")
    
# %% 1640.yıl==17.yy  109. yıl== 2.yy
print('********cell 11********')

from math import ceil

yil=input("hangi yili öğrenmek istersiniz? ")

yy=ceil(int(yil)/100)

print(yy,". yy'dasınız")
print(type(yil))
# %% 1640.yıl==17.yy  109. yıl== 2.yy
print('********cell 12********')

def yyhesapla(yil):
    if int(yil)>=1000 and yil[-2:]=='00':
        print(yil[:2],". yy'dasınız")
    elif int(yil)<1000 and yil[-2:]=='00':
        print(yil[:1],". yy'dasınız")
    elif int(yil)<100:
        print("1. yy'dasınız")
    elif int(yil)>1000:
        print(int(yil[:2])+1,". yy'dasınız")
    elif int(yil)<1000:
        print(int(yil[:1])+1,". yy'dasınız")
    
yyhesapla(yil)
# %% loops
print('********cell 13********')

for each in range(1,11):
    print(each)
    
for each in "ankara ist":
    print(each)

for each in "ankara ist".split():
    print(each)
    
i=0
while (i<4):
    print(i)
    i+=1
# %%
print('********cell 14********')
liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

a=liste[0]
for i in liste:
    if i<a:
        a=i
print(a)
# %%
