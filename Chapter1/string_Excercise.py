#1Create a string made of the first, middle, and last character
name = "James"
#calculate first and last letter first

first = name[0]
last = name[-1]

middle_index = int(len(name) / 2)
name1 = first + name[middle_index] + last
print("question1 ",name," its new string is ",name1)

################################
#Exercise 2. Create a string made of the middle three characters
def get_three_middle(str1):

#caclualting the middle index of string
    middle_index = int(len(str1) / 2) 
    print(str1[middle_index-1])
    print(str1[middle_index])
    print(str1[middle_index+1])
    
    
    print("question2 ",str1, "the three chars are ",str1[middle_index-1:middle_index+2])
str2 = "JhonDipPeta"
get_three_middle(str2)
##################################
#Exercise 3. Append new string in the middle of a given string
def get_into_middle(s1,s2):
    mid_s1 = int(len(s1)/2)
    new_str = s1[0:mid_s1] + s2 + s1[mid_s1:] 
    print("Question 3 ",new_str)    
s1 = "Aultt" 
s2 = "Kelly"
get_into_middle(s1,s2)
#################################
#Exercise 4. Create a new string made of the first, middle, and last characters of each input string
def join_middle(s1,s2):
    r1 = s1[0]
    r2 = s1[int(len(s1)/2)]
    r3 = s1[-1]
    t1 = s2[0]
    t2 = s2[int(len(s2)/2)]
    t3 = s2[-1]
    print ("Question 4", r1+t1+r2+t2+r3+t3)
m1 = "America"
m2 = "Japan"
join_middle(m1,m2)
###############################
#Exercise 5. Reverse a given string
str1 = "PYnative"
print("Question 5 ", str1[::-1])
#################################
#Exercise 6Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
l_postition = str1.rfind("Emma")
F_position = str1.find("Emma")
print("Question 6 ",l_postition ," and ", F_position)
# Excercise 7 Split a string on hyphens
# we have two straegy here one is finding the position of - 
str1 = "Emma-is-a-data-scientist"
print("completed question 7")
list1 = str1.split('-')
#for x in list1:
#    print(x)
# Exercise 8. Find all occurrences of a substring in a given string by ignoring the case
to_find = "USA"
str1 = "Welcome to USA. usa awesome, isn't it?"
str1=str1.lower()
temp_str = str1.count(to_find.lower())
print(temp_str)
#Exercise 9. String characters balance test
def string_balance_check(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
            break
    return flag

s1 = "yn"
s2 = "PyNative"
print("Is s1 and s2 balanced:", string_balance_check(s1, s2))

s1 = "ynf"
s2 = "PyNative"
print("Is s1 and s2 balanced:", string_balance_check(s1, s2))
#Exercise 11. Prefix/Suffix Check
str1 = "https://google.com"

# Check both start and end conditions
is_secure = str1.startswith("https")
is_com = str1.endswith(".com")

if is_secure and is_com:
    print("Is valid URL: True")
else:
    print("Is valid URL: False")
