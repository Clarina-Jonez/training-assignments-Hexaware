#Q1. Write a Python program to remove all duplicates from a list without using the set() function.
    # Input Example: [1, 2, 2, 3, 4, 4, 5]
    # Output: [1, 2, 3, 4, 5]

Input_List = [1, 2, 2, 3, 4, 4, 5]
Unique_List = []

for item in Input_List:
    if item not in Unique_List:
        Unique_List.append(item)

print("Output:",Unique_List)

#Q2. Given a list of integers, write a program to find the second highest unique number.
    #Input Example: [12, 5, 9, 21, 21, 3]
    #Output: 12
Int_list = [12, 5, 9, 21, 21, 3]
unique_list = []

for number in Int_list:
    if number not in unique_list:
        unique_list.append(number)

unique_list.sort(reverse=True)

if len(unique_list)>=2:
    print("Output:",unique_list[1])

#Q3. Rotate a list to the right by k positions.
    #Input: List = [1, 2, 3, 4, 5], k = 2
    #Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]
k = 2

rotated = list[-k:] + list[:-k]
print(rotated)

#Q4. Write a Python program to multiply the elements of each tuple in a list of tuples and return a new list.
    #Input: [(2, 4), (3, 5), (4, 6)]
    #Output: [8, 15, 24]

input_list = [(2, 4), (3, 5), (4, 6)]
output = []

for a,b in input_list:
    output.append(a*b)

print("Output",output)

#Q5. Given a tuple of integers, write a program to count how many times each element occurs.
#Input: (1, 2, 2, 3, 1, 4, 2)
#Output: {1: 2, 2: 3, 3: 1, 4: 1}

input_tuple = (1, 2, 2, 3, 1, 4, 2)
count_dict = {}

for num in input_tuple:
    if num in count_dict:
        count_dict[num]=count_dict[num]+1
    else:
        count_dict[num]=1

print("Output:",count_dict)


#Q6. Write a Python program to count the frequency of each character in a string using a dictionary.
    #Input: 'banana'
    #Output: {'b': 1, 'a': 3, 'n': 2}

input_new = 'banana'
count_freq_dict = {}

for letter in input_new:
    if letter in count_freq_dict:
        count_freq_dict[letter] = count_freq_dict[letter]+1
    else:
        count_freq_dict[letter] = 1

print("Output:",count_freq_dict)


#Q7. Merge two dictionaries such that common keys have their values summed.
#Input: {'apple': 10, 'banana': 5}, {'banana': 3, 'orange': 7}
#Output: {'apple': 10, 'banana': 8, 'orange': 7}

dict_1 = {'apple': 10, 'banana': 5}
dict_2 = {'banana': 3, 'orange': 7}
dict_result = {}

for key in dict_1:
    dict_result[key] = dict_1[key]

for key in dict_2:
    if key in dict_result:
        dict_result[key] += dict_2[key]
    else:
        dict_result[key] = dict_2[key]

print(dict_result)


#Q8. Given a dictionary of student names and their marks, print the name(s) of the student(s) with the highest
#marks.
    #Input: {'Alice': 85, 'Bob': 92, 'Carol': 92}
    #Output: ['Bob', 'Carol']

marks = {'Alice': 85, 'Bob': 92, 'Carol': 92}

highest = max(marks.values())

toppers = []

for name in marks:
    if marks[name] == highest:
        toppers.append(name)

print(toppers)

#Q9. Write a Python program to find all common elements among three lists using set operations.
    #Input: [1, 2, 3], [2, 3, 4], [3, 2, 5]
    #Output: {2, 3}

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [3, 2, 5]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

common = set1&set2&set3

print(common)


#Q10. From a sentence entered by the user, extract and display all unique words using a set.
    #Input: 'this is a test this is fun'
    #Output: {'this', 'is', 'a', 'test', 'fun'}

sentence = 'this is a test this is fun'
words = sentence.split()
unique_words = set(words)
print(unique_words)