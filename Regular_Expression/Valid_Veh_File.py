

f=open("VehicleNumbers","r")
fout=open("ValidReg","w")

regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))


from re import *
rule="KL\d{2}[A-Z]{1,2}\d{1,4}"


for vehiclenum in regnum:
    matcher=fullmatch(rule,vehiclenum)
    if matcher!=None:
        fout.write(vehiclenum+"\n")
    else:
        pass

#output can be seen in Vehiclereg file.

#create rule for validate gmail id
#validate all phone nos
#beautifulsoup packages bs4-webscrapping