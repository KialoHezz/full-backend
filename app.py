from new import Student
# OBJECTS $ CLASS
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# print(name,age)

# Inheritance
class Person(Student):
    pass

p1 = Person()
print(p1.name, p1.age)









# # write[w],read[r],append[a], reading/writtin[r+] and open a file
# # readable,readline,readlines
# # loop inside a file
# count_file = open('countries.txt', 'r')
# for files in count_file.readlines():
#     print(files)
# count_file.close()


# count_file = open('write.txt', 'w')
# count_file.write('woow')


