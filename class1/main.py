print("Hello, World!");

# name = "hiba"
# age=20

# print (name ,age )


# commentpy


                                           #data types 
food = "Biryani"   #string
price = 800        #integer
weight = 2.5       #float
is_available = True #boolean

print("Food: " + food)
print("Price: " + str(price))
print("Weight: " + str(weight))
print("Is Available: " + str(is_available))

Fruits = ["Apple", "Banana", "Mango", "Orange"]  #list
Fruits[2] ="Cherry" # to change the value of the list
Fruits[-1] ="Grapes" # to change the value of the list

print(Fruits)

Hospital=("Shifa", "Aga Khan", "Liaquat") #tuple
print("Hospitals------> " , Hospital)

Students_detials= {
    "Student_id": 12345,
    "Name": "Ali",
    "Age": 20
} #dictionary

ids={102,104,102,105,106} #set

print("Student Details------> " , Students_detials)
print(Students_detials["Name"])

print("IDs------> " , ids)



                                     #airthmetic_operations
x = 10
y = 5
print("Addition: ", x + y)
print("Subtraction: ", x - y)
print("Multiplication: ", x * y)
print("Division: ", x / y)
print("Modulus: ", x % y)
print("Exponentiation: ", x ** y)
print("Floor Division: ", x // y)


                    ##comparison_operators
print("Is x equal to y? ", x == y)
print("Is x not equal to y? ", x != y)
print("Is x greater than y? ", x > y)
print("Is x less than y? ", x < y)
print("Is x greater than or equal to y? ", x >= y)
print("Is x less than or equal to y? ", x <= y)


#logical_operators

print("Logical AND: ", x > 5 and y < 10)
print("Logical OR: ", x > 5 or y < 10)
print("Logical NOT: ", not(x > 5))


#conditional_statements
# is_raining = True

# if (is_raining == True):
#     print("It's raining. Take an umbrella.")
# else:
#     print("It's not raining. Enjoy your day!")

is_raining = input("Is it raining? yes/no: ")

if (is_raining == "yes"):
    print("It's raining. Take an umbrella.")
else:
    print("It's not raining. Enjoy your day!")


traffic_light =input("Enter the traffic light color (red, yellow, green): ")

if (traffic_light == "red"):
    print("Stop! The light is red.")
elif (traffic_light == "yellow"):
    print("Caution! The light is yellow.")
else:
    print("Go! The light is green.")

    student_percentage = float(input("Enter the student's percentage: "))
if(student_percentage >=90 and student_percentage <=100):
    print("Grade: A")
elif(student_percentage >=80 and student_percentage <90):
    print("Grade: B")
else:
    print("Grade: C")
