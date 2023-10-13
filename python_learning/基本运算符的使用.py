'''
>>> a = 7/2
>>> a 3.5
>>> a = 7//2
>>> a 3
>>> a = 7%2
>>> a 1
>>> 7%4
3
>>> 2**3 8
>>> 3/0
Traceback (most recent call last):
File "<pyshell#37>", line 1, in <module> 3/0
ZeroDivisionError: division by zero
>>> divmod(10,5) (2, 0)
>>> divmod(10,3) (3, 1)
'''


import time
a = time.time()
print(time.time())
b = int(time.time())
totalYears = b//365//60//24
print(totalYears)