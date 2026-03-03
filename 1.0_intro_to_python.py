# name = input('What is your name? ')
# print('Your name is ' + name)
print('Math')
print(type(2 + 4))
# ** - to the power of 
print(2 ** 8)
# // - double divide - returns a int and not a float - it rounds
print(5 // 3)

# % - modula - remainder of the division
print(6 % 2)

print('---------')

print('math functions')
 # round the number
print(round(3.1))
 # absolute number of the number
print(abs(-20))

print('---------')
# variables
print('variables') 
print('snake case - variables must have underscore : amali_age')
amali_age = 3
rozali_age = 1 
mathias_age = 36 
julia_age = 28 
total = julia_age+mathias_age+rozali_age+amali_age
print('Total age:') 
print(total)
# constnats - variable that does not change / use capitals
YEAR = 2026

print('------')
print('Expression and Statement')
print('line of code is statement')
print('expression is the function, result, etc...')

print('------')
print('strings - str')
#long string - use three '''
long_string = '''
here
i 
can 
write long strings
'''
print(long_string)

print('Escape sequence:')
weather = "It\'s \"kind of\" \nsunny"
# \ = anything after this is a string
# \t = tab 
# \n - new line in string
print(weather)

print('formatted strings')
# add f before the text - also use {} for variables
name = 'Amalia'
print(f'Hi {name}. You are {amali_age} years old')

print("square brackets []")
selfish = '01234567'
          #01234567
#take the index on 5 
print(selfish[5])
#take a sequence [start:stop]
print(selfish[0:5])
#[start:stop:stepover]
print(selfish[0:3:2])
#reverse order add a minus sig[-3]

print('-----')
print('strings are IMMUTABLE - create or destroy, cannot modify the original')
print('methods:')
print(name.upper())

print('-----')
print('booleans - bool - two options, true or false')
is_cool = False
is_cool = True

print('------')
print('Simple program: (hidden - commented in code')
#current_year = 2026
# birth_year = input('what year were you born? ')
#to get a integer as the current_year we add int() so math can work
#age = int(current_year) - int(birth_year)
#print(f'Your age is: {age}')

print('-----')
# password length program - 2.20.00

print('list')
print('use square brackets within variable')
list = [1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c']
list3 = [1,3,'a',True]

# dictionary - mulitple values and variables in one area
user = {
    'basket':[1,2,3],
    'greet': 'hello',
    'age': 20
    }
    
print('does something exist in dictionary?')
print('basket' in user)
print('update:')
print(user.update({'age' :23}))
print(user)

print('------')
print('Tuple - list but cannot modify them - it is immutable')

print('------')
print('Set')
my_set = {1,2,3,4,5}
my_set.add(100)
my_set.add(2)
your_set = {4,5,6,7,8,9}
# 2 is not added as it is already in the set - must be unique
my_list = [5,6,7,7,7,7,8,9,10]

#change this list to a set - removes all duplicates 
print(set(my_list))
print(my_set) # my_set is printed after above code

print('DIFFERENCE:')
print(my_set.difference(your_set))  # the difference between sets

print('DISCARD:')
print(my_set.discard(100))  # 100 is discarded from my_set
print(my_set) # my_set is printed after difference and discard

print('INTERSECTION:')
print(my_set.intersection(your_set))

print('UNION:') # united the sets, removed duplicates, created new
print(my_set.union(your_set))
#also can write as: 
print(my_set | your_set)

print('\n')
print('AI RULES')
print('1. save you time \n2. should not add complexity')

print('\n')
print('QUESTIONS FOR AI')
print('1. Explain this code... ')
print('2. Make this code more efficient... ')

print('\n')
print('Conditional logic')
print('QESTTION: Can you drive?')
is_old = False
is_licenced = True

if is_old and is_licenced:  # and - this means and - both must be true
    print('Yes, you are old enough to drive.')
#elif condition1: 
    #print()
#elif condition2:  # can have many many elif 
    #print()
else:
    print('Not old enough!')
    
# is - chceks for the exact thing 
# == - equality of two things 

print('\n')
print('LOOPS')  # use for 
# iterable - list, dictionary, tuple, set, string
# iterate - one by one check each item in the collection
for item1 in (1,2,3,4,5):
    print(item1)
    
user = {
    'name': 'Mathias',
    'age': 35,
    'can_swim': True 
    }

for item in user:  # get the keys - variables
    print(item)

for item in user.values():  # get the values 
    print(item)

for item in user.keys():  # get the values 
    print(item)
    
for key, value in user.items():  # get the values 
    print(key, value)
    
    
print('\n')
print('COUNTER')  # count the items in our list
my_list2 = [1,2,3,4]
counter = 0  # counter variable must be set before for
for item in my_list2:
    counter = counter + item
print(counter)  # print must be outside code block


print('\n')
print('RANGE')

for _ in range(0, 10, 2): # range of 0-10 and stepover 2, or countdown -2 etc.. 
    print(_)


print('\n')
print('ENUMERATE')    
for i,char in enumerate('Hello'):
    print(i, char)
    

print('\n')
print('WHILE')    
i = 0
while i < 50:
    print(i)
    i += 1    # +=  increment it, is same as =i+ 
#    break    # break out of the while loop 

#while True:
#    response = input('say something: ')
#    if (response == 'bye'):
#        break
    
    
print('\n')
print('First GUI')        
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]
for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')
    
# iterate over picture
# if 0 - print ''
# if 1 - print *



print('\n')
print('FUNCTIONS') 
def say_hello():
    print('hello')  # here the function is created
say_hello()   # here the function is called and executed
# we can define a whole block of code as a funciton - this cleans the code
def show_tree():   # here the tree image is created as a function 
    for image in picture:
        for pixel in image:
            if (pixel == 1):
                print('*', end='')
            else:
                print(' ', end='')
        print('')

show_tree()   # here i call the show_tree image 

# function should do one thing really well
# should return something

def my_add(num1, num2):
    return num1 + num2
    
total = 15 
print(my_add(10,total))



print('\n')
print('METHODS')
print('Methods must be owned by something - whatever is left to the method it is owned by it')

print('\n')
print('DOC STRINGS')
def test(a):
    '''
    Info: this fucntion tests and pritnts param a
    '''
    # add comments and definitions to functions created
    
print(test.__doc__)  # prints the info about test function


print('\n')
print('ARGUMENTS and KeyWordArguments')
# *args **kwargs 

def super_func(*args):   # can accept any amount of positional arguments 
    return sum(args)

print(super_func(1,2,3,4,5))

print('create a program that prints the highest even from list')
def highest_even(li):  
    evens = []    # create a new list that has only evens
    for item in li:  # for item in list,
        if item % 2 == 0:  # if item is divided by 2 exactly
            evens.append(item)  # append (add) to evens
    return max(evens)
    
print(highest_even([10,2,3,4,8,11]))



print('\n')    # 8.01 time 
print('Walrus operator')




print('\n')    
print('Scope')
# what variables do i have access to? 

print('\n')
print('Command line - Terminal')
print(' dir = lists everything in current directory\n cd = current directory \n cls = clears the screen \n echo. = create something, like a file \n start. = opens something \n rename = renames the file, folder \n del = delete a file \n deltree = delete folder ')



