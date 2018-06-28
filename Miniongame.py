import re

s = input().upper()
vowels = re.compile("[A,E,I,O,U]")
pts_a = 0
pts_b = 0
ptsk = ['Kevin', 0]
ptss = ['Stuart', 0]
t = 0
len_s = len(s)

#print (len(s))

for i in s:
    t = t + 1
    if re.match(vowels,i):
        for n in range(len(s)-(t-1)):
            strg = (s[t-1:n+t])
            ptsk[1] = ptsk[1] +1
    else:
        for n in range(len(s)-(t-1)):
            strg = (s[t-1:n+t])
            ptss[1] = ptss[1] +1
if (ptss[1] == ptsk[1]):
    print ("Draw")
else:
    p = max(ptsk[1],ptss[1])
    if p in ptsk:
        print (ptsk[0], end=" ")
        print (ptsk[1])
    else:
        print (ptss[0], end=" ")
        print (ptss[1])
