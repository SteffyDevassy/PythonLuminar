#start with a-k
#2nd char should be digit and divisible by 3
#followed by any no. of chars
from re import *

#match and fullmatch


# rule='[a-kA-K][369]\w*'
# rule='[a-kA-K][369][a-zA-Z0-9]*'
rule='[a-kA-K][369]\w*'
var=input("Enter variable name")
matcher=fullmatch(rule,var)
if matcher!=None:
    print("valid")
else:
    print("Invalid")