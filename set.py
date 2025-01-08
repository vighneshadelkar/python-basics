#set, they are unordered so index operations like set[0] are not possible
basket={"orange","apple","mango"}
s=set()
s.add(1)
s.add(2)
s1={2,3,1,8,9,4}
s2={2,3,4,1,20}
subset={2,4}
#union of two ser
union=s1|s2

#intersection
inter=s1&s2

#diff
diff=s1-s2

#subset
print(s1<s2) #false {2,3} would have been a right ans 

print(union,inter,diff)
#FROZEN SET DOES NOT ALLOW TO ADD NEW ELEMENT

fs=frozenset([1,2,3,1,2,3])

print(basket,s,fs)

print(type(basket))