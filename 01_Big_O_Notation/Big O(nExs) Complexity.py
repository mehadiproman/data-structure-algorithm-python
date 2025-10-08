# def generate_permutations(arr, start=0):
#     """
#     Generates all permutations of the array 'arr'
#     """
#     if start == len(arr) - 1:
#         print(arr)  # O(1) per permutation
#     else:
#         for i in range(start, len(arr)):
#             # Swap current index with start
#             arr[start], arr[i] = arr[i], arr[start]  # O(1)
#             # Recursively generate permutations for the rest
#             generate_permutations(arr, start + 1)  # Recursive call
#             # Swap back to restore original array (backtracking)
#             arr[start], arr[i] = arr[i], arr[start]  # O(1)

# # Example usage
# numbers = [1, 2, 3]
# generate_permutations(numbers)

#------------------------------------------------------------------------------------------

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)



# n = 12
# print(factorial(n))

#------------------------------------------------------------------------------------------

# def all_cubes(items):
#     result = []              # Step 1: create an empty list

#     for item in items:       # Step 2: loop through each element in the list
#         result.append(pow(item, 3))  # O(n) # Step 3: cube the number and add to result
#         print(result)        # Step 4: print the list after each addition

# items = [2, 3, 5, 7]
# all_cubes(items)

#------------------------------------------------------------------------------------------

def all_cubes(items):

    for item in items:      
        result=(pow(item, 3))   # O(1)
        print(result)     

items = [6, 5]

all_cubes(items)

# print(x.bit_length())  # shows how many bits are needed to store the number 100
print(all_cubes(items).bit_length())  # shows how many bits are needed to store 