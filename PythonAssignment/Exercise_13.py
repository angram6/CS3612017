import re

file = open('emails.txt','r')
file = file.read()

matches = re.findall(r'([\w\.-]+@[\w\.-]+)', file)
print(matches)

