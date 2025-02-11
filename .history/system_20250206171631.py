import sys   # Import the system module

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   if index == 0:
      print ('当前水果 :', 'pass')
      continue;
   if index == 2:
      break;
   else:
      print ('当前水果 :', fruits[index])


flag = 'banana' not in fruits;  # True
del fruits[0]
print(flag, fruits)

print([1,3,3,4,5,6,7,8,9,10].count(3))  # None