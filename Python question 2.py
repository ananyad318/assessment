#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Python
# Question 2

from collections import Counter

def highest_frequency_word_length(input_str):
    words = input_str.split()
    word_counts = Counter(words)
    
    if not word_counts:
        return 0
    
    max_word = max(word_counts, key=word_counts.get)
    max_length = len(max_word)
    
    return max_length

# Example usage
input_str = "write write write all the number from from from 1 to 100"
result = highest_frequency_word_length(input_str)
print(result)


input_str = "apple orange banana apple orange banana orange"
result = highest_frequency_word_length(input_str)
print(result)  


# In[ ]:





# In[ ]:




