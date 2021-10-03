password = ''

while password != "python123":
    password = input("Enter Password: ")
    if password != 'python123':
        print("Wrong Password, please try again!")
print("Access Granted!\n")




emails = ['jra@hotmail.com','ka@gmail.com','cya@gmail.com','rata@hotmail.com']


print("ALL EMAILS: ")
for i in emails:
    print(i)
print("\n")


print("ONLY HOTMAILS: ")
for i in emails:
    if 'hotmail' in i:
        print(i)
