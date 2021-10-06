file = open("D:\\Python Tutorial\\learning-python\\CODE\\Files\\file1.txt","r")
print(type(file))
content = file.read()

print(content)
print(type(content))

file.seek(0)

content2 = file.readlines()

print(content2)
print(type(content2))

print(content2[0])

for lines in content2:
    print(lines)

content3 = [i.rstrip("\n") for i in content2]

print(content3)

file.close()
