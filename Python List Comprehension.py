# Python List Comprehension


type([1,2,3,4,5,6])

lst=[]
for i in range(0,8):
    lst.append(i)

# print(lst)

lst=[1,2,3,4,5,6]
lst2=[]
for i in lst:
    lst2.append(i**2)

# print(lst2)

numbers=[1,2,3,4,5]
squared_numbers=[i**2 for i in numbers]
# print(squared_numbers)

## Filtering even numbers from a list:
numbers=[1,2,3,4,5,6,7,8,9,10]
even_number=[n for n in numbers if n%2==0]
# print(even_number)

##Flattening a list of lists: 2 for loops
lists=[[1,2,3],[4,5,6],[7,8,9]]
flattend_list=[item for sublist in lists for item in sublist]
# print(flattend_list)

# Generating a list of the first letters of words
words=['apple','banana','cherry','date']
first_letters=[word[0] for word in words]
# print(first_letters)

## Generating a list of the squares of even numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
even_number=[n**2 for n in numbers if n%2==0]
# print(even_number)

## Converting a list of strings to a list of integers
strings=['1','2','3','4','5']
integ=[int(s) for s in strings ]
# print(integ)

## Generating a list of the fibonacci series using a list comprehension
fib=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]
fibno=[fib[i-1] + fib[i-2] for i in range(2,len(fib))]
# print(fibno)

## Generating a list of all the divisors of a number:
number=36
nu =[i for i in range(1,number+1) if number%i==0]
print(nu)