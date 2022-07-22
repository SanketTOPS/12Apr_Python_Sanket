import re

mystr="This is Python!"

x=re.match('is',mystr)
y=re.search('is',mystr)
print(x)
print(y)

