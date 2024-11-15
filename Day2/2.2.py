#Type Error , Type Checking , Type Conversion

len("Hello")

print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

#Type conversion
print(int("123") + int("456"))
int()
float()
str()
bool()

# Task:
#print("Number of letters in your name: " + len(input("Enter your name")))

# Answer:
name_of_user   = input("Enter your name")
length_of_name = len(name_of_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))



