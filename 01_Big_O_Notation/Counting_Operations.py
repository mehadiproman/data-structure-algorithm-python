students = ['Andrew', 'Akshat', 'Chrish', 'Harshit', 'lary', 'Shubham', 'Tim', 'Drake', 'Ashish']  # O(1)

def randomFunction(students):
    first = students[0]        # O(1) → Accessing an element by index is constant time
    total = 0                  # O(1) → Simple variable assignment
    new_list = []              # O(1) → Empty list creation

    for student in students:   # Loop runs n times
        total += 1             # O(n) → Executes once per iteration
        new_list.append(student)  # O(n) → Each append is O(1), repeated n times → total O(n)

    print(new_list)            # O(1) → Printing once
    return total               # O(1) → Return statement

print(randomFunction(students))  # Overall: O(3 + 2n + 2) → simplified to O(n)
