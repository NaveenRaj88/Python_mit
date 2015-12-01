__author__ = 'anandran'

# varA = -2
# varB = "goodbye"
# if type(varA)== str or type(varB)== str:
#     print("string involved")
# elif varA > varB:
#     print("bigger")
# elif varA == varB:
#     print("equal")
# elif varA < varB:
#     print("smaller")
#
#
#
#
# num = 10
# while num > 3:
#     num -= 1
#     print num
#
#
#     num = 0
# while num > 10:
#     num +=2
#     print num
# print("Goodbye!")
#
#
#
#
#
# loop=0
# sum=0
# end = 6
# while loop <= end:
#     sum = sum+loop
#     loop +=1
# print sum




# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print char
#     else:
#         numCons -= 1
#
# print 'numVowels is: ' + str(numVowels)
# print 'numCons is: ' + str(numCons)





# num = 10
# for num in range(5):
#     print num
# print num




# for letter in 'hola':
#     print letter


# count = 0
# for letter in 'Snow!':
#     print 'Letter # ' + str(count) + ' is ' + str(letter)
#     count += 1
#     break
# print count
#
# for variable in range(20):
#     if variable % 4 == 0:
#         print variable
#     if variable % 16 == 0:
#         print 'Foo!'


# print("Hello!")
# for num in range(10, 2, -2):
#     if num % 2 == 0:
#         print num





# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print "Iteration " + str(iteration) + "; count is: " + str(count)
#     iteration += 1



count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)