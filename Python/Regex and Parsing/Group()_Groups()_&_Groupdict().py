# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S=input()
#print(S)
m=re.match(r'.*?([a-z0-9A-Z])\1', S)
if m is None:
    print(str(-1))
else:
    print(m.group(1))
