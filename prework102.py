##Question 1
#def hello_name(user_name):
# every function takes input (or no input)
# does a transformation or action
# and gives back some output (can be no output)
def sup(user_inputioso):
    print(f'whats up {user_inputioso}, do you know what -updog- means?')
sup('Tatyana')




#Question 2
#Print first 100 odd numbers in Python.

need2exerciseOrAaronGoesInsane = [x for x in range(1, 200, 2)]
print(need2exerciseOrAaronGoesInsane)



##Q3
#Please write a Python function, max_num_in_list to return the max number of a given list.
#  The first line of the code has been defined as below.
def max_num_in_list(a_list):
        return max(a_list)
print(max_num_in_list([11, 5, 4,2, 77777, 392 ]))
#Q4
##Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def leapin(yur):
    return (yur % 400 == 0) or ((yur % 4 == 0) and (yur % 100 != 0))
leapin(1200)



#Q5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, 
#[2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.
def consecutive(a_list):
    for i in range(0, len(a_list)-1):
        if a_list[0]+1 != a_list[i+1]:
            return False
        else:
            return True
consecutive([1, 2, 4, 66, 4])
consecutive([6, 7, 8, 9, 10, 11])


