

f=open("MobileNumbers","r")
fout=open("ValidMob","w")

mobnum=set()
for numbers in f:
    mobnum.add(numbers.rstrip("\n"))


from re import *
rule="90\d{8}"


for Mobilenum in mobnum:
    matcher=fullmatch(rule,Mobilenum)
    if matcher!=None:
        fout.write(Mobilenum+"\n")
    else:
        pass