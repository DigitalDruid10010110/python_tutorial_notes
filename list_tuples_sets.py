# Notes
# Lists, Tuples, Sets
courses = ['History', 'Math', 'Physics', 'CompSci'] # list (square brackets)  (index starts at 0)  (index is the position of the element in the list)

print(courses)  # ['History', 'Math', 'Physics', 'CompSci']

print(len(courses))  # 4

# Slice (range of index) (start:stop) (start:stop:step) (stop is not included in the range of index)

print(courses[0])  # History (index 0) (first element) (position 1) (start) 

print(courses[3])  # CompSci (index 3) (fourth element) (position 4) (end)

print(courses[-1])  # CompSci (index -1) (last element) (position 4) (end)

print(courses[0:2])  # ['History', 'Math'] (index 0 to 2) (first to third element) (position 1 to 3) (start to end)

print(courses[:2])  # ['History', 'Math'] (index 0 to 2) (first to third element) (position 1 to 3) (start to end)

print(courses[2:])  # ['Physics', 'CompSci'] (index 2 to end) (third to last element) (position 3 to 4) (start to end)

# Add an element to the end of the list (append method)

courses.append('Art')  # add an element to the end of the list (append method)

print(courses)  # ['History', 'Math', 'Physics', 'CompSci', 'Art'] (Art added to the end of the list)

# Add an element to a specific position in the list (insert method)

courses.insert(0, 'Art')  # add an element to the beginning of the list (insert method)

print(courses)  # ['Art', 'History', 'Math', 'Physics', 'CompSci', 'Art'] (Art added to the beginning of the list)

courses_2 = ['Art', 'Education']  # list (square brackets)

courses.insert(0, courses_2)  # add a list to the beginning of the list (insert method)

print(courses)  # [['Art', 'Education'], 'Art', 'History', 'Math', 'Physics', 'CompSci', 'Art'] (list added to the beginning of the list)

print(courses[0])  # ['Art', 'Education'] (index 0) (first element) (position 1) (start)

print(courses[0][1])  # Education (index 0, 1) (first element, second element) (position 1, 2) (start, next)

# Add multiple elements to the end of the list (extend method)

courses.extend(courses_2)  # add multiple elements to the end of the list (extend method)

print(courses)  # [['Art', 'Education'], 'Art', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Art', 'Education'] (list added to the end of the list)

# Remove an element from the list (remove method)

courses.remove('Math')  # remove an element from the list (remove method)

print(courses)  # [['Art', 'Education'], 'Art', 'History', 'Physics', 'CompSci', 'Art', 'Art', 'Education'] (Math removed from the list)

# cont at 9:05 in the video