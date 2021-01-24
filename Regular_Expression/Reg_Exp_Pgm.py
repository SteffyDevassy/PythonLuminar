from re import *
#---------------------------------#
#predefined character sets
# --------------------------------#

pattern1='[a-k]' #check for lowercase a to z
pattern2='[0-9]' #check for all digits
pattern3='[^0-9]' #except no.s
pattern4='[^a-z]' #except lowercase characters
pattern5='[a-zA-Z]' #check for both lower and upper case characters
pattern6='[^a-zA-Z0-9]'


#--------------------------#
#predefined Charachters
#-------------------------#
pattern7="\s"  #check for spaces
pattern8="\S"  #Except spaces
pattern9="\d" #digits
patterns="\D"    #except digits
patterns1="\w" #a-zA-Z0-9
pattern="\W"  #special charachters only



matcher=finditer(pattern,"abc Z@7k")

for match in matcher:
    print(match.start()) #returns index
    print(match.group()) #returns group string

out=[(match.start,match.group()) for match in matcher]
print(out)