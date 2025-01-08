# list set dict comprehension

#reduces the numebr of line
nums=[1,2,3,4,5,6,7]

even=[num for num in nums if num%2==0]

sqr=[num*num for num in nums]

print(even,sqr)

s=set([1,2,3,1,2,3])

print(s)

even_set={num for num in s if num%2==0}
print(even_set)

cities=["mumbai","delhi","chennai"]
countries=["india","china","uk"]

z=zip(cities,countries)
dict={city:country for city,country in zip(cities,countries)}
print(dict)
for a in z:
    print(a)
    
#('mumbai', 'india')
#('delhi', 'china')
#('chennai', 'uk')