
# coding: utf-8

# In[1]:


#Name: Rishabh Kedia


# In[89]:


import numpy as np


# In[104]:


#Create matrix A with size (3,5) containing random numbers
a = np.random.random(15).reshape(3,5)
print('A: %s' %a)


# In[105]:


#Find the size and length of matrix A
print('A size: %s' %a.size)
print('A length: %s' %a[0].size)


# In[106]:


#Resize (crop/slice) matrix A to size (3,4)
a = a.flatten()[0:12].reshape(3,4)
print('A: %s' %a)


# In[107]:


#Find the transpose of matrix A and assign it to B
b = a.T
print('B: %s' %b)


# In[108]:


#Find the minimum value in column 1 of matrix B
print('Minimum value in column 1 of matrix B: %s' %np.min(b[:,0])) #means each row in the first column or 0th index column


# In[109]:


#Find the minimum and maximum values for the entire matrix A
print('Max in A: %s' %np.max(a))
print('Min in A: %s' %np.min(a))


# In[110]:


#Create vector X (an array) with 4 random numbers
x = np.random.random((4))
print('X: %s' %x)


# In[111]:


#Create a function and pass vector X and matrix A in it
#In the new function multiply vector X with matrix A and assign the result to D
def multiply(a, x):
    return a*x


# In[112]:


d = multiply(a, x)
print('D: %s' %d)


# In[113]:


#Create a complex number Z with absolute and real parts != 0
z = 2 + 3j


# In[114]:


#Show its real and imaginary parts as well as it’s absolute value
print('Z Real: %s' %np.real(z))
print('Z Imaginary: %s' %np.imag(z))
print('Z Absolute: %s' %np.abs(z))


# In[115]:


#Multiply result D with the absolute value of Z and record it to C
c = d * np.abs(z)
print('C: %s' %c)


# In[116]:


#Convert matrix B from a matrix to a string and overwrite B
print('B: %s' %np.array_str(b.flatten()))


# In[117]:


#Display a text on the screen: ‘Your Name is done with HW2‘
print('Rishabh Kedia is done with HW2')

