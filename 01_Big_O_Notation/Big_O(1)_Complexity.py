student_list = ['Andrew', 'Akshat', 'Chrish', 'Harshit', 'lary', 'Shubham', 'Tim', 'Drake', 'Ashish']

def displayStudent(student_list):
    print(student_list[0])
    print(student_list[2])
    print(student_list[3])
    print(student_list[4])
    print(student_list[5]) # O(1)+O(1)+O(1)+O(1)+O(1)=O(1)

displayStudent(student_list)

# Time Complexity: O(1)
# Because we are accessing fixed indices (0, 2, 3, 4, 5) of the list.
# No matter how large the list is, the number of accesses does not change,
# so the runtime remains constant.