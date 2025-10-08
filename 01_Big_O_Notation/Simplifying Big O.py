#Rule 4 Consider different variable for different inputs
num_list =[1, 2, 3, 4, 5, 6, 7]

def rondomFunction(num_list, char_list):
    for num in num_list: print(num) #0(n)
    for num in num_list: print(num) #0(n)


    print(rondomFunction(num_list, char_list)) #0(n + n)


num_list = [1, 2, 3, 4, 5, 6, 7]
char_list = ['a', 'b', 'c', 'd', 'e']

def rondomFunction(num_list, char_list):
    for num in num_list:
        print(num) #0(n)
    for char in char_list: 
        print(char) #0(m)

print(rondomFunction(num_list, char_list)) #O(n + m)