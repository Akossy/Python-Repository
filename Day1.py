# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
print ("Hello World Juliana")

firstname = "Juliana"
lastname = "Boateng"
print ("Hello " + firstname + " " + lastname)



input ("Please tell me your first name ? ")
input ("Please tell me your last name ?")
# print (" Hello "" first name answer_2 =)


name = "Ryan,Paul,Wright"
#str.lower() converts string to lower case
print (name.lower())
#str.upper() convert string to upper case
print(name.upper())
# #str.replace() replaces old substring with new
print(name.replace("Wright", "Lastname"))
#str.split() returns a list of words in the string we can sepcify the seperator inside the parenthesis
# print(name.split(","))
#str.join() concatenates a iterable or collection of strings
print(" join ".join(['Ryan', 'Paul', 'Wright']))
#str.count() returns number of non-overlapping occurances of substring in string
print(name.count("a"))
#str.isdigit() Return true if string digital string,
# otherwise str1 = "Cat" #return false str2 = "123" #returns true str3 = "12.24" #returns false only accepts digits
str1= "cat"
str2= "123"
str3= "Sleep"

print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())

#concatination combining stings together
# print("dog" + "cat")#returns dogcat
# print("dog", "cat")#return dog cat

name = "Juliana"
school = "High"
age = 49
maths = True
testscore = 50.6
print("My name is", name, "My age is", age, "Maths:", maths, "My test score is", testscore)
#f strings allows us to combine multiple datatypes in a string aswell as perform calculations within curly bracketsprint
print(f"My name is {name}, my age is {age-10}, Maths: {maths}, My testscore is {testscore}")
# you can add in the curly brackets
print("Hello my name is \"ryan\"")
#returns Hello my name is "ryan"
print('Hello my name is \\ryan\\')
# #returns Hello my name is \ryan\
print('Hello \n my name is ryan')#
# returns Hello
# my name is ryan
print('Hello \t my name is ryan')
#returns Hello my name is ryan
# print("Hello my name is ryan \U0001F604")
# #returns Hello my name is ryan 😄



print  (3, "Hello")
# this is a comment and will be ignored
# how to find oout data type
print (type(3.0))



#covertings turns one type of data in to another
print (float(3))
#will return 3.0 a intergar to a decimal
print (int(3.6))
#will return 3



