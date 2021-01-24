f=open("EmailAddress", "r")
fout=open("ValidEmail","w")

emailset=set()
for id in f:
    emailset.add(id.rstrip("\n"))

from re import *
#  '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
rule='[a-z0-9\._]@gmail.com'

for validEmail in emailset:
    matcher=fullmatch(rule,validEmail)
    print(matcher)
    if matcher!=None:
        fout.write(validEmail+"\n")
    else:
        pass

