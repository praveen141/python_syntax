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


