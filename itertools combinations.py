Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Enter your code here. Read input from STDIN. Print output to STDOUT
... from itertools import combinations
... 
... s , n  = input().split()
... for i in range(1, int(n)+1):
...     for j in combinations(sorted(s), i):
