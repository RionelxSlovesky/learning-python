file=open("D:\\Python Tutorial\\learning-python\\CODE\\Files\\file2.txt","w")

file.write("Line 1\n")

file.write("Line 2\n")

l = ["Line 3","Line 4","Line 5","Line 6"]

for line in l:
    file.write(line+"\n")

file.close()
