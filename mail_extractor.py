import re
fname = input('ENTER FILE NAME -')
fh = open(fname)
l = list()
for line in fh:
    line = line.rstrip()
    email = re.findall('\S+?@\S+',line)
    if len(email) !=0:
        for id in email:
            l.append(id)
print (*l, sep ='\n')
