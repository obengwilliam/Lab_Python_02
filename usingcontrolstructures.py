'''
creator:obeng william
description:even and odd numbers
'''


theInput = raw_input("Enter an integer: ")
if int(theInput)%2==0:
    print "The input is even"
elif int(theInput)%2==1:
    print "The input is odd"

for  i in range(39,-1,-3):
...      print i


    
        
primarysch_age=6
voting_age=18
president_age=50
retire_age=70
personAge=input("Enter an age:")
if personAge<4:
    print "You are too young for school"
elif personAge==voting_age:
    print "Remember to vote"

elif personAge==retire_age:
      print "too Old"


if personAge==president_age:
     print "Vote for me"
else:
     print "You can not be president"



#exercis 7

for i in range(39,-1,-3):
    print i
    
#exercise 8
for i in range(6,30):
    if i%2==0:
       continue;
    if i%3===0:
        continue;
    if i%5==0:
        continue
    print i




#exercise 9
i=0;
start=True
while start:
 if (79*i)%97==1:
     print i,"\n"
     start=False
 i=i+1
     


