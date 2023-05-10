Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#!/bin/python3

import math
import os
import random
import re
import sys
... 
... # Complete the time_delta function below.
... from datetime import datetime
... def time_delta(t1, t2):
...     time_format = '%a %d %b %Y %H:%M:%S %z'
...     t1 = datetime.strptime(t1, time_format)
...     t2 = datetime.strptime(t2, time_format)
...     return str(int(abs((t1-t2).total_seconds()))) 
... 
... if __name__ == '__main__':
...     fptr = open(os.environ['OUTPUT_PATH'], 'w')
... 
...     t = int(input())
... 
...     for t_itr in range(t):
...         t1 = input()
... 
...         t2 = input()
... 
...         delta = time_delta(t1, t2)
... 
...         fptr.write(delta + '\n')
... 
