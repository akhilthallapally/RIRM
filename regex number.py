#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Python program to check if
# given mobile number is valid
import re
 
def isValid(s):
     
    # 1) Begins with 0 or 91
    # 2) Then contains 6,7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
    return Pattern.match(s)
 
# Driver Code
s = input("")
if (isValid(s)):
    print ("Valid Number")    
else :
    print ("Invalid Number")


# In[ ]:




