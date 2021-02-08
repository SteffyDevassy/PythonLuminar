st={2,4,67,8}
print(st)

# st1= {12,23,23}
# print(type(st1))
# print(st1)
# st2={12,22,33}
# st1.update(st2)
# print(st1)


#-------------------
#union
st={10,20,30,40,50}
st1={40,50,60}
un=st.union(st1)
print(un)

#intersection
st={10,20,30,40,50}
st1={40,50,60}
inter=st.intersection(st1)
print(inter)


#diff

st={10,20,30,40,50}
st1={40,50,60}
diff=st.difference(st1)
print(diff)
