# Reading data from the file

obj = open('../../../Documents/Notes/QAENGR.txt', 'w')


#Read all data from the file
# print(obj.read())

#Read specific line from the file
print(obj.readline(2,))

#Read all characters from file and display 1 by 1
for i in obj.read():
    print(i)

#Read all data from file line by line

s = obj.readline()
while(s):
    print(s)
    s = obj.readline()