# Given a string, determine if it is a palindrome, considering only alphanumeric 
# characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Time O(n) Space O(n)
from collections import deque
def validPalindrome(string):
    if string == "":
        return True
    stack = deque()
    for char in string:
        if char.isalnum():
            stack.append(char.lower())
    for char in string:
        if char.isalnum():
            current = stack.pop()
            if current != char.lower():
                return False
    return True

#Time O(n) Space O(1)
def validPalindromeMaster(string):
    if string == "":
        return True
    i = 0
    j = len(string) -1
    while i < j:
        while i < j and not string[i].isalnum():
             i += 1
        while i < j and not string[j].isalnum():
            j -=1
        if string[i].lower() != string[j].lower():
            return False
        i += 1
        j -=1
    return True

def main():
    good = 'A man, a plan, a canal: Panama'
    bad = 'race a car'
    edge = ".,"
    print(validPalindrome(good))
    print(validPalindromeMaster(edge))




if __name__ == "__main__":
    main()