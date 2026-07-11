#Why python is called as dynamically typed language
math = 50
Chem= 60
Phy = 70
Pi= 3.14
name= "Vedant Kavitkar"
print( type(math))
print(type(chem))
print(type(phy))
print( type(Pi))
print(type (name))
# python interpreter takes the responsibility to assign the data type 

#how to check the address of any variable?=using ans id()
math = 50
Chem= 60
Phy = 70
Pi= 3.14
name= "Vedant Kavitkar"
print( id(math))
print(id(chem))
print(id(phy))
print( id(Pi))
print(id (name))
#id function is user to written the adress of variable or obj

#wap to accept the three papers marks and calculate total marks, percentage 
#and display 

phy = 50
chem = 60
math = 70
total= phy+chem+math
percentage= total/ 3.0
print("total marks=",total)
print("percentage=", percentage)

#What is typecasting 

#int() used to convert in integer 
print (int(3.14))
print (int(true))#=1
print (int(false))#=0
print(int("4.22"))
print(int ("4"))
#priny(int("vedant"))
#we can not convert complex value to int
#we can not convert floating point value string to int 
#cant convert string name 

# float() used to convert
print(float(3)) #3.0
 #print (float(50+2j))
 print(float(True))# 1.0
print(float(False))# 0.0
print (float(4.22))
printf(float("4"))
#print(float("name"))
#we can not convert complex value to float 

## complex() used to convert
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
#print(complex("name"))
print(complex(5,-3))
print(complex (True, False))


## bool() is used to convert
print(bool(0)) # False
print(bool(15))#True
print(bool(3.14)) #True
print(bool(0.0))# False
print(bool(1+2j))# True
print(bool(0+0j))# False
print(bool(-1)) #True
print(bool (False)) #False
print(bool (True)) #True
print(bool ("Vedant"))

Swapping of two variable using third 

x = 5
y = 10
x = x + y  # x 15
y = x - y  # y 5
x = x - y  # x 10


principal= int(input("Enter principal Amount: "))
rate_of_intrest = int(input("Enter the rate of interest:"))
time = int(input("enterprises the duration of loan amount:"))

simple_intrest = 0
principal* rate_of_interest *time/100
print("simple intrest amount=" , simple _intrest)

Calculate the area of circle 

pi =3.14
r =10
Area= pi*r*r
print(area)


Circumference 
pi =3.14
r =10
circumference= 2* pi*r
print(circumference)

h = 5.7
inch= h* 12
cm = inch*2.54
print(inch)
print(cm)


# Reverse a 3-digit number
num = 123
a = num // 100      # 1
b = (num // 10) % 10 # 2
c = num % 10         # 3
rev = c * 100 + b * 10 + a
print("Reverse =", rev)


centi= float(input("enter the temp in centi"))
f =( 1.8 * centi) + 32
print( "tempreture in fahrenheit =", f )
 
#Special operator's 
There are two types of special operator's 
#The main function of identity operator is adress comparison 
#2 types 
Is
Is not

For wx 
A=-10
B=10

Output 10