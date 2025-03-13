# Create a python script:

# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console 
# Each line of code should be commented with description.

# Commit script to git repository and provide link as home task result.


import random

def generate_list_of_number(start, end, size):
    '''
    Function to generate the list of number
    '''
    n = 100  # Number of random numbers
    li = random.sample(range(start, end), size)
    return li

def sort_list(l1):
    '''
    Function to sort the list of number
    '''
    sorted_list = []
    for i in range(0, len(l1)):
        for j in range(i+1, len(l1)):
            if l1[i] >= l1[j]:
                l1[i], l1[j] = l1[j],l1[i]
    return li

def calculate_average(l1):
    '''
    Function to calculate the average of the list 
    '''
    list_len = len(l1)
    total_sum = 0
    for i in l1:
        total_sum = total_sum+i

    return total_sum/list_len

if __name__ == "__main__":
    even_number = []
    odd_number =[]
    li = generate_list_of_number(0,1000,100)
    sorted_list = sort_list(li)
    for i in  sorted_list:
        if i%2==0:
            even_number.append(i)
        else:
            odd_number.append(i)
    print(calculate_average(odd_number), " average of odd no")
    print(calculate_average(even_number), " average of even no")
