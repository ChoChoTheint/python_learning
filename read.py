# file = open('./text.txt')
# for line in file:
#     print(line)

# file.seek(0) #cursor move to first char
# print(file.read(100)) # read only 100 word

# print(file.close())

# listline = file.readline()
# print(listline)


with open('./text.txt') as file: # no need to close
    for line in file:
        print(line)