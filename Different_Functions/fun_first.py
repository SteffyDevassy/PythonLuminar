# def add(n1,n2):
#     res=n1+n2
#     print(res)
# add(10,20)


#variable length argument methods

# def add(*num):
#     s=0
#     for n in num:
#         s=s+n
#     print(s)
#
# add(2,3,4)


def print_data(**num):
    print(num)
print_data(birthpalce="kochi",desig="dev",sal=2400,work="aluva")


#kwags =>passing  no. of values as dictionary
def print_data(**num):
    for k,v in num.items():
        print(k,v)
print_data(birthpalce="kochi",desig="dev",sal=2400,work="aluva")