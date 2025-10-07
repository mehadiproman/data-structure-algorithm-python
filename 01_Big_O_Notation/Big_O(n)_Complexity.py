student_list1 = ['Tim', 'Daraka', 'ashish', 'Alo']
student_list2 = ['andrew', 'Chrish', 'Harshit', 'Lary', 'Proman']


def checkStudent(student_list1):
    for student in student_list1:
        if student == 'Alo':
            print('Available!')
        else:
            print('Not available!')

checkStudent(student_list1) # Its print not available 4 time cause of every elements in the list iterate


# Big O ---> List search (Linear path) → O(n)
# The time complexity is O(n) because the program checks each element
# in the list one by one until it finds 'Proman' or reaches the end.
# Each comparison (student == 'Proman') takes constant time O(1),
# and doing this for all n elements makes the overall complexity O(n).



# student_list1 = ['Tim', 'Daraka', 'ashish'] 
# student_list2 = ['andrew', 'Chrish', 'Harshit', 'Lary', 'Proman']

# def checkStudent(student_list):
#     if 'Tim' in student_list:
#         print('Available!')
#     else:
#         print('Not available!')

# checkStudent(student_list1)