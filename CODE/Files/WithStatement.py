with open("D:\\Python Tutorial\\learning-python\\CODE\\Files\\file2.txt","a+") as file:
    file.seek(0)
    content = file.read()
    file.write("Line 11\nLine 12")

print(content)
