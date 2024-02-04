#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python
# Question 1
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17],
]

target = 5
result = search_matrix(matrix, target)

if result:
    print(f"Target {target} found in the matrix.")
else:
    print(f"Target {target} not found in the matrix.")


# In[ ]:





# In[ ]:




