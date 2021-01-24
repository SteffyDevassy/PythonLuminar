#regular expression for pattern matching

#step 1:
#Package not in builts.py .So
import re
matcher=re.finditer("ab","ababababbbbabbabab")
# for match in matcher:
#     print(match.start())
#     print(match.group())

cnt=0
for match in matcher:
    # print(match.start())
    cnt+=1
print(cnt)