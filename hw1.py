#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

##### input

#to get the input for which we have to find the root

print("enter the input to find the root")
m=int(input())

#to get the power of the root(eg: square root or cube root)

print("enter the the power of the root")
power=int(input())

# using built in function to find the square root in decimal
v=int(math.sqrt(m))

# to format(eg: to display the output as 4 root 5 which is the square root of 80 instead of the decimal format) 
for x in range(1,v+1):
    sq=x**power
    if(m%sq==0):
        o1=x
        o2=int(m/sq)

##### output        
        
# to print the formatted output        
if(o2>1):        
    print(o1,u"\u221A",o2)
else:
    print(o1)


# In[2]:


##### input

# to get the long integer value
print("enter the long integer value")
m=input()

# to get the int to be subtracted from each digit 
print("enter the value to subtract")
n=int(input())

size=len(m)

# to initialize the output 
s=""

#to subtract for each integer 
for i in range(size-1):
    o=int(m[i])
    #if the difference is greater append the same
    if(o-n>0):
        s=s+str(o-n)
    #else append the zero    
    else:
        s=s+"0"
        
##### output

#to display the output 
print(s)


# In[ ]:




