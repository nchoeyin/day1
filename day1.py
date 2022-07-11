#!/usr/bin/env python
# coding: utf-8

# In[1]:


# playing with variables to manage data
name = input("Enter your name: ")
print(len(name))


# In[3]:


import sys
name = input("Enter your name: ")
print(sys.getsizeof(name)) #gets the number of bytes


# In[4]:


name = "Jack"
name = "Arnold"
print(name)


# In[6]:


print("Bonjour! Welcome to the band name generator ") #crreating the band name generator
city = input("Which city did you grow up in: ")
pet_name = input("Enter your pet name: ")
band_name = city+" "+pet_name
print("Your band name is "+band_name)


# In[ ]:




