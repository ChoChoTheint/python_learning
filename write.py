# with open('./about.txt','w') as file:
#     file.write('I am ChoCho')

# with open('./about.txt','a') as file:
#     file.write('\n I am 23 year old')


lists = ['I am chocho','\n I am 24 year old']
with open('./about.txt','a') as file:
    file.writelines(lists)