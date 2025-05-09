# Reading data from the file

obj = open('../../../Documents/Notes/QAENGR.txt', 'a')
#a = append
#w = overwrite
#r = read

#Read all data from the file
print(obj.read())

#Read specific line from the file
print(obj.readline(2,))

#Read all characters from file and display 1 by 1
for i in obj.read():
    print(i)

#Read all data from file line by line

s = obj.readline()
while(s):
    print(s)

#Write data to text
obj.write("HELLO WORLD")
obj.close()

print(obj.tell())
obj.seek(5)
print(obj.tell())


