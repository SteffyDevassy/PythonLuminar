# for i in range(1,13):
#     print(i)


#1 2 3 4
#5 6 7 8
#9 10 11 12
#method 1
# cnt=0
# for i in range(1,13):
#     print(i,end="\t")
#     cnt+=1
#     if cnt==4:
#         print("\n")
#         cnt=0

#method 2
cnt=0
for i in range(1,13):
    print(i,end="\t")
    cnt+=1
    if i%4==0:
        print()
