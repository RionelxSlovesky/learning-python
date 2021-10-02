def ageIn50Years(age):
    newAge = int(age) + 50;
    print("Your age in 50 years is: " + str(newAge))

age = input("Enter your age: ")

age = int(age)

if age<150:
    print("your age is " + str(age))
    ageIn50Years(age)
else:
    print("How is that possible?")
