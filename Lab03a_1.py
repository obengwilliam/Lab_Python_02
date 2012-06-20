import math
number_tobe=input('input numbers for a reverse encryption')

width=math.ceil(math.log(number_tobe,10))
width=int(width)
check=width-1
encrypt=int(number_tobe)
ans=0

for i in range(width):
    value=encrypt/10
    remainder=encrypt%10
    ans=ans +remainder *10**(check-1)
    encrypt=value
print ans

    
    

