from re import *
pattern1= "a"   #chk for all and returns a
pattern2="a+"  #check for a and more than one a OR consecutive a
pattern3="a*"   #check for all postions and returns a
pattern4="a?"    #chk for all positions and returns a
pattern5="^a"    #chk the given string is starting with a
pattern6="a$"      #chk the given string is end with a
pattern7='a{2,3}'    #returns min_2_a and max_3_a
pattern="^a"
matcher=fullmatch(pattern,"aaabaababaaa")
if matcher!=None:
    print("Given string starting with a")
else:
    print("string is not start with a")
# for match in matcher:
#     print(match.start())
#     print(match.group())