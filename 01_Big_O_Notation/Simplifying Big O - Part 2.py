num_list = [1, 2, 3, 4, 5, 6, 7]

def randomFunction(num_list):
    total = 0  # O(1) → simple variable assignment, constant time
    all_integer = True  # O(1) → another simple assignment, constant time

    for num in num_list:
        print(num)  # O(n) → loop runs once per element in num_list

    for num1 in num_list:
        for num2 in num_list:
            print(num1, num2)  # O(n^2) → nested loop, n*n iterations
            total += 1  # O(n^2) → inside nested loop, runs n*n times

    msg = "Rule 5 - Remove all non-dominents"  # O(1) → string assignment, constant time
    return total  # O(1) → returning a value, constant time

# The total time complexity:
# O(1 + 1 + n + n^2 + n^2 + 1 + 1) → simplifies to O(n^2)
print(randomFunction(num_list))