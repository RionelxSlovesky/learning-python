file=open("D:\\Python Tutorial\\learning-python\\CODE\\Files\\file2.txt","a")

l = ["Line 7","Line 8","Line 9","Line 10"]

for line in l:
    file.write(line+"\n")

file.close()
