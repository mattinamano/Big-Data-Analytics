#!/usr/bin/env python
# coding: utf-8

# In[16]:


# To find which lockers will be open among the 1000 lockers, 

    # as a sample lets consider 10 lockers (L1-L10) and 10 students(S1-S10) toggling the lockers 

    # where the S1 toggles all lockers and Sn toggles every nth locker

    # L1 # L2 # L3 # L4 # L5 # L6 # L7 # L8 # L9 # L10 #   
#S1 #  o #  o #  o #  o #  o #  o #  o #  o #  o #   o #
#S2 #  o #  x #  o #  x #  o #  x #  o #  x #  o #   x #
#S3 #  o #  x #  x #  x #  o #  o #  o #  x #  x #   x #
#S4 #  o #  x #  x #  o #  o #  o #  o #  o #  x #   x #
#S5 #  o #  x #  x #  o #  x #  o #  o #  o #  x #   o #
#S6 #  o #  x #  x #  o #  x #  x #  o #  o #  x #   o #
#S7 #  o #  x #  x #  o #  x #  x #  x #  o #  x #   o #
#S8 #  o #  x #  x #  o #  x #  x #  x #  x #  x #   o #
#S9 #  o #  x #  x #  o #  x #  x #  x #  x #  o #   o #
#S10#  o #  x #  x #  o #  x #  x #  x #  x #  o #   x #

#--- conclusion1: number of time the locker was opened and closed = the no of factors the locker number has---#

    # eg. locker 1: 

        ### Number of time the locker was opened and closed =1
        ### The no of factors the locker 1 has = 1

    # eg. locker 4: 

        ### Number of time the locker was opened and closed =3
        ### The no of factors the locker 1 has = 3

#--- conclusion2: Since all the lockers where closed initially, Lockers with odd number of factors will be open---#

    # eg. locker 9: 

        ### Number of time the locker was opened and closed =3
        ### The no of factors the locker 9 has = 3

        ### opened by Student1 -->closed by Student 3-->opened by student 9

        ### locker 9 with odd number of factors, ends up being open


#---Soln: To find which lockers will be open among the 1000 lockers, its enough to find the lockers with odd number of factors--# 

    ### hint: All perfect sqaures have odd number of factors

# A list to store all the open lockers
open_lockers=[]

# To count the total number of open lockers
cnt=0

# To find the perfect squares(As they only have odd number of factors i.e the lockers that are open ) 

for i in range (1,1000):
    j = 1;
    while j*j <= i:
        if j*j == i:
            open_lockers.append(i)
            cnt=cnt+1
        j = j+1
    i = i+1

# To print the lockers that will be open among the 1000 lockers     
print("The open lockers are ",open_lockers)

# To print the number of open lockers
print("The total number of open lockers =",cnt)


# In[15]:


### optimized prime function to determine Mersenne primes

def isPrime(m_prime) :   
    if (m_prime <= 1) : 
        return False
# all primes are of the form 6k ± 1, with the exception of 2 and 3 and we know that they are prime so they are set explicitly set to return true
    if (m_prime <= 3) : 
        return True
# if its divisible by 2 or 3 then its not a prime so set to return False
    if (m_prime % 2 == 0 or m_prime % 3 == 0) : 
        return False
    i = 5
# checking till √n to decrease the time complexity from o(n) to o(square root of n)
    while(i * i <= m_prime) : 
        if (m_prime % i == 0 or m_prime % (i + 2) == 0) : 
            return False
# As we know that all primes are of the form 6k ± 1, with the exception of 2 and 3, we increment by 6
        i = i + 6
    return True

m_prime_candidates=[] ### to store all integers of the form 2^n-1 with n ranging from 2 to 32
m_primes=[]           ### to store all integers of the form 2^n-1 with n ranging from 2 to 32 that are prime
n=[]                  ### to store the values of n that generate valid primes

for i in range(2,33): 
    cur_m_prime=pow(2,i) - 1
    
    # adding all integers of the form 2^n-1 with n ranging from 2 to 32 (i.e) all Mersenne prime candidates
    
    m_prime_candidates.append(cur_m_prime)
    
    m_primes.append(cur_m_prime)
    
    # testing all of the candidates to see if they’re actually prime 
    
    if(isPrime(cur_m_prime)):
        n.append(i) ### tracking the values of n that generate valid primes,
        
    else:    
        m_primes.remove(cur_m_prime) ### Removing the candidates that aren’t prime   
        
### Displaying the result
        
print("The Mersenne prime candidates in the range 2 to 32 are ",m_prime_candidates)
print("The Mersenne primes in the range 2 to 32 are ",m_primes)
print("Values of n that generate valid primes",n)


# In[ ]:




