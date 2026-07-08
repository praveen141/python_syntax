#Excercise1
student = {"name": "Alice", "age": 20, "grade": "B"}
# Add a new key
to_update = {"city": "Newyork"}
student.update(to_update)
# Modify an existing key
student["age"]=21  
#print(student["name"]) 
###########
#Excercise2Write a Python program to remove a specific key from a dictionary,
#  retrieve all key-value pairs, and check whether a given key exists.
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
# to remove specifc key
car.pop("model")


#etrieve all key-value pairs
print(car)
# to check value exist yes

print("year exists: ", "year" in car)
print("cost exists: ", "cost" in car)

#Excercise 3 merge two list to create disctionary
keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]
student = dict(zip(keys, values))
print(student)
#Excercise 4 clear valeus from dictionary
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
inventory.clear()
print(inventory)
#Excercise 5 to merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1 = dict1 | dict2
#dict1.update(dict2)
print(dict1)
#Excercise 