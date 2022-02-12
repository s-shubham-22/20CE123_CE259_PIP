t = int(input()) # User Input: No. of Test Cases

li = [] # Empty List

for i in range(4): # Taking Strings from User
    li.append(input())

li_dict = list(dict.fromkeys(li)) # Removing Repeating Elements

print(len(li_dict)) # Printing Number of Non Repeating Elements

for i in li_dict: # Printing Counts of every element Repeated in List
    print(li.count(i), end = " ")

print() # New Line

# Student ID: 20CE123
# Student Name: Shubham Sareliya
# Aim: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output 
#     order should correspond with the input order of appearance of the word. See the sample input/output for 
#     clarification. 
# Github Repo Link: https://github.com/s-shubham-22/20CE123_CE259_PIP
