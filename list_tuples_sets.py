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

courses2 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

courses2.append('Art')  # add an element to the end of the list (append method)

print(courses)  # ['History', 'Math', 'Physics', 'CompSci', 'Art'] (Art added to the end of the list)

# Add an element to a specific position in the list (insert method)

courses3 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

courses3.insert(0, 'Art')  # add an element to the beginning of the list (insert method)

print(courses)  # ['Art', 'History', 'Math', 'Physics', 'CompSci'] (Art added to the beginning of the list)

courses4 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

courses_2 = ['Art', 'Education']  # list (square brackets)

courses4.insert(0, courses_2)  # add a list to the beginning of the list (insert method)

print(courses4)  # [['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci'] (list added to the beginning of the list)

print(courses4[0])  # ['Art', 'Education'] (index 0) (first element) (position 1) (start)

print(courses4[0][1])  # Education (returns the second element of the first element of the list) (index 0, 1) (first element, second element) (position 1, 2) (start, next)

# Add multiple elements to the end of the list (extend method)

courses4.extend(courses_2)  # add multiple elements to the end of the list (extend method)

print(courses)  # ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education'] (list added to the end of the list)

# Remove an element from the list (remove method)

courses4.remove('Math')  # remove an element from the list (remove method)

print(courses4)  # ['History', 'Physics', 'CompSci'] (Math removed from the list)

courses5 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

courses5.pop()  # remove the last element from the list (pop method)

print(courses5) # 'History', 'Math', 'Physics'(Compsci removed from the list)

popped = courses5.pop()  # remove the last element from the list and assign it to a variable (popped method)    

print(popped)  # Compsci (Compsci removed from the list and assigned to the variable) 

# Reverse the order of the list (reverse method)

courses6 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

courses6.reverse()  # reverse the order of the list (reverse method)

print(courses6)  # ['CompSci', 'Physics', 'Math', 'History'] (list reversed)

# Sort the list in ascending order (sort method)    

courses7 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

courses7.sort()  # sort the list in ascending order (sort method)

nums = [1, 5, 3, 4, 2]  # list (square brackets)

nums.sort()  # sort the list in ascending order (sort method)

print(nums)  # [1, 2, 3, 4, 5] (list sorted in ascending order)

print(courses7)  # ['CompSci', 'History', 'Math', 'Physics'] (list sorted in ascending order)

# Sort the list in descending order (sort method)

courses8 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

nums2 = [1, 5, 3, 4, 2]  # list (square brackets)

nums2.sort(reverse=True)  # sort the list in descending order (sort method) 

print(nums2)  # [5, 4, 3, 2, 1] (list sorted in descending order)

courses8.sort(reverse=True)  # sort the list in descending order (sort method)

print(courses8)  # ['Physics', 'Math', 'History', 'CompSci'] (list sorted in descending order)

# Sort the list in ascending order without changing the original list (sorted function)

courses9 = ['History', 'Math', 'Physics', 'CompSci']  # list (square brackets)

sorted_courses = sorted(courses9)  # sort the list in ascending order without changing the original list (sorted function) must be assigned to a variable

print(sorted_courses)  # ['CompSci', 'History', 'Math', 'Physics'] (list sorted in ascending order)

print(courses9)  # ['History', 'Math', 'Physics', 'CompSci'] (original list unchanged)

# Sort the list in descending order without changing the original list (sorted function)

# cont. video 13:40

