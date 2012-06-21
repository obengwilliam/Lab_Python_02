'''
Created on Jun 21, 2012

@author: william
'''
#EXTRA CREDIT
import math  #IMPORTING MATH MODULE

number=raw_input("Pleas input numbers")
number_int=int(number)
length_num=int((math.log(number_int,10))) + 1
add_length=length_num
reverse=0
reverse2=0

for i in range(length_num):
    num_step1=number_int/10
    num_remainder=number_int%10
    add_length=add_length-1
    reverse+=num_remainder *(10**(add_length))
    number_int=num_step1
print reverse  



#QUESTION ON EXERCISE TWO
add_length=length_num #TRYING TO GET LENGTH
number_int=int(number) #CONVERTING INT TO NUMBERS
for i in range(length_num):
    num_step1=number_int/10
    num_remainder=number_int%10
    num_remainder=(num_remainder+7)%10
    add_length=add_length-1
    reverse2+=num_remainder *(10**(add_length))
    number_int=num_step1
print reverse2 #PRINTING ANSWER EG 12345 BECOMES 89012 















