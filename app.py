# tuple
my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(my_list[1][1])
# loop in loops
for list in my_list:
    print(list)
    for row in list:
        print(row)

# loops for loops,while loops
# condition
i = 2
while i > 1:
    print(i)

list = ['ji','ja','jo']

for values in list:
    print(values)

# function
def greet():
    name = 'hezron'
    print('hello' + ' ' + name)

greet()

# # # dictionary function > type,key,value
dict = {
    "name":"hezron",
    "qualifications":['SQL','PYTHON','WEB DEVT',],
    "friends": "woow" 
}

print(dict)
# # list > index number
# # list(())
# #  list methods > extend,insert,remove
countries =  ['kenya', 'Uganda', 'somalia','U.S.A']
print(countries[0])
print(countries[0][1].upper())
print(countries[1:])

countries =  ['kenya', 'Uganda', 'somalia','U.S.A']
music_countries = ['rock','regge']
countries.extend(music_countries)
print(countries)

# # variable
name = "Hezron"

print ("Hello"+ " "+ name)

# # datatypes > string,numbers
# # string functions, index,uppercase,lowercase,len
# # isupper used to return a boolean (TRUE or FALSE  )
print(name[1].upper())
print(len(name))
# # index of character
print(name.index('z'))
# replace
print(name.replace('z', 'M'))
# value type
print(type(name))
# # numbers > operation multiplication *,division /,addition +,subtraction - ,modulor %

sentence = input('enter your sentence')

word1 = input('enter the word to replace: ')
word2 = input('enter the word to replace it with: ')

print(sentence.replace(word1, word2))

