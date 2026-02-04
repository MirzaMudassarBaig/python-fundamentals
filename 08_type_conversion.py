x=10   #int
y=10.2  #float
z="hello"  #string
print(type(x))
print(type(y))
print(type(z))

x=x*y
print(type(x))

#implicit type conversion
x=x+y
print(x,"type of x is:", type(x))

#explicit type conversion
age=input("what is your age? ")
#age=int(age)
print(type(int(age)))

#name
name=input("what is your name? ")
print(type(str(name)))

# name=input("what is your name? ")
# print(type(int(name)))            type conversion error

#type_conversion