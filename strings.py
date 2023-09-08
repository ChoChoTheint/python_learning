# print('hello' + ' ' + 'world')
# print('Repation ' * 2)

# name = 'john'
# print('Hello, %s' % name)

# first = 'john'
# last = 'smith'
# print('Hello, %s %s' % (first, last))


# one = 1
# two = 2.0
# three = 'three'

# print("Counting: %d, %f, %s" % (one, two, three))

# y = 1.15656565656
# print("More: %.8f, Less: %.4f, Even less: %.1f" % (y,y,y))

# x = 14
# print('Int: %d, lowercase x: %x, uppercase x: %X' % (x,x,x))



x = 'Hello world'

# length
print(len(x))            # prints: 11

# character position
print(x.index('o'))      # prints: 4

# counting occurrences
print(x.count('l'))      # prints: 3

# transforming
print(x.upper())         # prints: hello world
print(x.lower())         # prints: HELLO WORLD

# splitting
print(x.split(" "))      # Prints: ['Hello', 'world']
print(len(x.split(" "))) # Prints: 2


# string slicing
print(x[3:7]) # prints: lo w

# single character capturing
print(x[3]) # prints: l

# slicing to end-of-string
print(x[3:]) # prints: lo world

# slicing from beginning-of-string
print(x[:7]) # prints: Hello w

# slicing last n characters
print(x[-3:]) # prints: rld

print(x.startswith('Hello')) # prints: True
print(x.endswith('rld'))    

print(x[1:7:2]) # prints: el

# string reversing, using stepping
print(x[::-1]) 