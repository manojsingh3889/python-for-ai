import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

first_name = "manoj"
last_name = 'singh'
myAge= 25
isAdult = True


#string
string = "My name is Manoj Singh"
long_string = """
My name is manoj singh.
I am 36 years old
"""

full_name = first_name + " " + last_name


long_dash = "_" * 50
print(len(long_dash))

length_of_name = len(full_name)

voting_age = 18
can_vote = myAge >= voting_age 

# f string
driving_min_age = 16
has_license = True
print(f"can drive:{myAge >= driving_min_age and has_license}")

# if, elif, else
temperature = 31

if temperature > 30:
    print("its very hot")
elif temperature > 25:
    print("its hot")
else:
    print("its a nice weather!")

# loop
for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0,10, 2):
    print(i)


#Data Structure
##Lists
my_list = ["Alice", 25, myAge, True, has_license]
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[-5])

my_list[0] = "Dave" # update
my_list.append("Alice")
print(my_list)
my_list.remove("Alice")
print(my_list)
my_list.insert(1, "ALICE")
print(my_list)
print(my_list.index("ALICE"))


##Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person.get("age"))
print(person["age"])
person["license"] = True

print(person)

print(person.keys())
print(person.values())
print(person.items()) #returns as entry or items


##tuple
#immutable data structure
#empty
empty = ()

#Tuple with items
point = (3,5)
colors =( "red", "green", "blue")

print(empty)
print(point)
print(colors)

##set
#data set for unique values
#empty
empty_set= set()
 #with value - both ways work
numbers={1,2,3,4,5}
fruits = set({"apple", "banana"})

#from list
set_my_list = set(my_list)

print(f"my_list = {my_list}\nset_my_list = {set_my_list}")

