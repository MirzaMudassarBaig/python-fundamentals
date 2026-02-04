#while  and for loops


#while loop
x=0
while x<=5:
     print(x)
     x=x+1

#forloop
for x in range(4,11):
     print(x)

#array
days= ("mon","tues","wed","thurs","fri","sat","sun")

for d in days:
   if (d=="fri"):break #loop stop
   if (d=="fri"):continue #skip d
   print(d)