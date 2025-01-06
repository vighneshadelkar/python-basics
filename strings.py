# strings

# strings are immutable, u can replace the entire string but no change a specific character of string
text="ice cream"

# 0 1 2 3 4 5 6 7 8
# i c e   c r e a m

print(text[0]) #i
print(text[1]) #c

#the below line would give typeError
# text[2]="g" 

# slicing
print(text[0:3]) # "ice"
print(text[:3]) # "ice" start from index 0
print(text[4:]) # "cream" end at last index

# instead of \n
address='''1 new york
usa'''
print(address)

# concatenate two strings using "+"
string="hello" + "world"
print(string) # "helloworld"
# we can join two strings but we cannot as number to string
num=1
# print("0"+num) #error

string="0" + str(num)
print(string) # "01"
