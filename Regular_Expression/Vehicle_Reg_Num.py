#KL08BS1375  ->valid
#GJ08BN2211  ->Invalid
from re import *
rule='[KL][0-9]{2}[A-Z]{2}[0-9]{1,4}'
# rule="KL\d{2}[A-Z]{2}\d{1,4}"
vehicle=input("Enter reg no")
matcher=fullmatch(rule,vehicle)
if matcher!=None:
    print("Valid")
else:
    print("Invalid")