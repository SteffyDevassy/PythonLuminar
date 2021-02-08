pattern="ABABAC"
#find first recursive character :A
word=" "
for i in range(0,len(pattern)):
    if(pattern[i] not in word):
        word+=pattern[i]
    else:
         print("First Recursive Character is",pattern[i])
         break