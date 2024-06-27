## Why Function?
# 1. to make code more readable
# 2. to make code more efficient
# 3. to make code more maintainable
# 4. to make code more reusable
# 5. to make code more extensible


## Function

def welcome(msg):
    # Maintainable
    """
    Description: This function will show a welcome message
    
    Return: This function will return the welcome message
    """
    return msg

msg=welcome("Welcome all")    
# print(msg)

## Function to add even and odd number.

def even_odd_sum(lst):
    """
    Description: This function will add even and odd number in a list.

    Return: This function will return the sum of even and odd number in a list.
 
    """
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
           even_sum+=i
        else:
           odd_sum+=i
    return even_sum,odd_sum
 

sum=even_odd_sum([1,2,3,4,5,6,7,8,9,10])
print(sum)
