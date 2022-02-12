def lapindrome(string): # Function to check if a string is a lapindrome
    string = [item for item in string] # Convert string to list
    string_front = string[0:len(string)//2] # Split string into two halves
    if len(string) % 2 == 0: # If string is even
        string_back = string[len(string)//2:]
    else: # If string is odd
        string_back = string[len(string)//2+1:]
    string_front.sort() # Sort the front half
    string_back.sort() # Sort the back half
    if string_front == string_back: # If the two halves are equal
        return True # Return True
    else: # If the two halves are not equal
        return False # Return False

t = int(input()) # Number of Test Cases

li = [] # Empty List

for i in range(t): # Input String in List 
    li.append(input())

for i in li: # Check if lapindrome
    if lapindrome(i):
        print("YES")
    else:
        print("NO")

# Student ID: 20CE123
# Student Name: Shubham Sareliya
# Aim: Lapindrome is defined as a string which when split in the middle, gives two halves having the same 
#   characters and same frequency of each character. If there are odd number of characters in the string, we 
#   ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two 
#   halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few 
#   examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters 
#   but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a 
#   lapindrome. 
# Github Repo Link: https://github.com/s-shubham-22/20CE123_CE259_PIP
